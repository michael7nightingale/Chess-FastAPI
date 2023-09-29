from fastapi import WebSocket, APIRouter, Path, Request, Depends
from starlette.websockets import WebSocketDisconnect
from fastapi_authtools import login_required
from datetime import datetime
from functools import wraps
from itertools import chain
from random import shuffle

from api.dependencies.database import get_game_repository, get_socket_repository
from package.chess.chessboard import Chess
from db.repositories import UserRepository, GameRepository


router = APIRouter(prefix="/chess")
player_colors = {"white", "black"}


class WaitConnectionManager:
    """
    Class for managing waiting players.
    """
    def __init__(self):
        self.connections: dict = {}

    async def connect(self, websocket, username: str) -> None:
        if len(self.connections):
            game_repo: GameRepository = get_socket_repository(GameRepository)()
            user_repo: UserRepository = get_socket_repository(UserRepository)()
            enemy_username, enemy_websocket = list(self.connections.items())[-1]
            self.connections.pop(enemy_username)

            # colors
            colors = list(player_colors)
            shuffle(colors)
            you_color, enemy_color = colors
            # users
            you = user_repo.get_by(username=username)
            enemy = user_repo.get_by(username=enemy_username)
            black_user, white_user = (you, enemy) if you_color == "black" else (enemy, you)
            new_game = game_repo.create(
                black_user=black_user.id,
                white_user=white_user.id,
            )
            # game data to send
            game_data = {
                "status": 201,
                "you": username,
                "enemy": enemy_username,
                "game_id": new_game.id,
                "you_color": you_color,
                "enemy_color": enemy_color
            }
            # send game data
            await enemy_websocket.send_json(game_data)

            enemy_game_data = {
                "you": game_data['enemy'],
                "enemy": game_data['you'],
                "you_color": game_data['enemy_color'],
                "enemy_color": game_data['you_color'],
                "status": game_data['status'],
                "game_id": game_data["game_id"]
            }
            await websocket.send_json(enemy_game_data)

        else:
            self.connections[username] = websocket

    async def start_game(self, game_id: str, data: dict) -> None:
        for ws in self.connections[game_id]:
            await ws.send_json(data)


wait_connection_manager = WaitConnectionManager()


@router.websocket("/ws/wait-player")
async def wait_for_the_plater(
    ws: WebSocket,

):
    """Endpoint for waiting for players in the queue."""
    await ws.accept()
    username = await ws.receive_text()
    await wait_connection_manager.connect(websocket=ws, username=username)
    while True:  # to save websocket connection
        await ws.receive_text()


class ChessConnectionManager:
    """
    Class for managing active games.
    """
    def __init__(self):
        self.connections: dict = {}

    async def connect(self, websocket, game_id: str) -> None:
        """On connecting websocket."""
        if game_id in self.connections:
            match len(self.connections):
                case 0:
                    self.connections[game_id]['chessboard'] = Chess()
                    self.connections[game_id]["users"].append(websocket)
                case 1:
                    self.connections[game_id]["users"].append(websocket)
                case _:
                    await websocket.close()
        else:
            self.connections[game_id] = {
                "users": [websocket],
                "chessboard": Chess(),
            }

    async def broadcast(self, game_id: str, data: dict) -> None:
        """Send data to all users` websockets associated with the game."""
        for ws in self.connections[game_id]['users']:
            await ws.send_json(data)

    async def move(self, game_id: str, data: dict) -> None:
        """Make a move for the game chessboard."""
        chessboard = self.connections[game_id]["chessboard"]
        if chessboard.access_color == data['color']:
            to_move = chessboard.move(data["cell_id"])
            if to_move is not None:
                (from_id, to_id), (from_data, to_data), move_signal = to_move
                move_data = {
                    "status": 200,
                    "to_id": to_id,
                    "from_id": from_id,
                    "from_data": from_data,
                    "to_data": to_data,
                    "move_user": data["user"],
                    "move_color": data["color"],
                    "new_color": chessboard.access_color
                }
                if move_signal is chessboard.CheckAndMateSignal:
                    move_data.update(status=303)
                    game_repo = get_socket_repository(GameRepository)()
                    user_repo = get_socket_repository(UserRepository)()
                    game = game_repo.get(game_id)
                    if move_data['move_color'] == "black":
                        winner = game.black_user
                    else:
                        winner = game.white_user
                    winner_user = user_repo.get(winner)
                    message = f"Game is over. Player {winner.usename} won ({move_data['move_color']})"
                    move_data.update(
                        winner=winner_user.username,
                        message=message
                    )
                    game_repo.finish(game_id, winner=winner)

                await self.broadcast(game_id, move_data)

    async def finish_game(self, game_id: str, data) -> None:
        for user in self.connections[game_id]['users']:
            user: WebSocket
            finish_data = {
                "message": "The game is finished.",
                "status": 303,
            }
            await user.send_json(finish_data)
        del self.connections[game_id]

    async def interrupt_game(self, game_id: str, websocket: WebSocket) -> None:
        for user in self.connections[game_id]['users']:
            if user != websocket:
                user: WebSocket
                finish_data = {
                    "message": "The game is interrupted.",
                    "status": 401,
                }
                await user.send_json(finish_data)
                await user.close()
        game_repo = get_socket_repository(GameRepository)()
        game_repo.update(game_id, time_finish=datetime.now())
        del self.connections[game_id]


chess_connection_manager = ChessConnectionManager()


def game_context(func):
    @wraps(func)
    async def inner(ws: WebSocket, game_id: str = Path()):
        try:
            result = await func(ws, game_id)
            return result
        except WebSocketDisconnect:
            return await chess_connection_manager.interrupt_game(game_id, ws)
        except Exception as e:
            print(e)

    return inner


@router.websocket('/ws/{game_id}')
@game_context
async def sock_chess(
        ws: WebSocket,
        game_id: str = Path(),
):
    """Endpoint for playing chess game."""
    await ws.accept()
    await chess_connection_manager.connect(websocket=ws, game_id=game_id)
    while True:  # listening for moves
        data: dict = await ws.receive_json()
        await chess_connection_manager.move(game_id, data)


@router.get("/my-games")
@login_required
async def get_my_games(
        request: Request,
        game_repo: GameRepository = Depends(get_game_repository)
):
    white_games = game_repo.filter(black_user=request.user.id)
    black_games = game_repo.filter(white_user=request.user.id)
    return sorted(
        chain(black_games, white_games),
        key=lambda game: game.time_start
    )


@router.get("/rules")
async def get_rules():
    with open("docs/rules.txt") as file:
        return file.read()
