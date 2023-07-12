from fastapi import WebSocket, APIRouter, Path, Depends
import asyncio
import json
from random import choice, shuffle

from package.chess import Chess
from api.dependencies import get_repository, get_socket_repository
from infrastructure.db.repositories import UserRepository, GameRepository


router = APIRouter(
    prefix="/ws"
)
player_colors = {"white", "black"}


class WaitConnectionManager:
    """
    Connection manager for waiting-for-players lobby.
    """
    def __init__(self):
        self.connections: dict = {}

    async def connect(self, websocket, username: str) -> None:
        """
        If there are not any players, put player into queue, else take the last player and go playing.
        """
        if len(self.connections):
            game_repo: GameRepository = get_socket_repository(GameRepository)()
            user_repo: UserRepository = get_socket_repository(UserRepository)()
            enemy_username, enemy_websocket = list(self.connections.items())[0]
            self.connections.pop(enemy_username)

            # colors
            colors = list(player_colors)
            shuffle(colors)
            you_color, enemy_color = colors
            # users
            you = user_repo.filter(username=username)
            enemy = user_repo.filter(username=username)
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
            await websocket.send_json(game_data)
            
            enemy_game_data = {
                "you": game_data['enemy'],
                "enemy": game_data['you'],
                "you_color": game_data['enemy_color'],
                "enemy_color": game_data['you_color'],
                "status": game_data['status'],
                "game_id": game_data["game_id"]
            }
            await enemy_websocket.send_json(enemy_game_data)

        else:
            self.connections[username] = websocket


wait_connection_manager = WaitConnectionManager()


@router.websocket("/wait-player")
async def wait_for_the_plater(
    ws: WebSocket,

):
    """Endpoint for waiting for other players. """
    await ws.accept()
    username = await ws.receive_text()
    await wait_connection_manager.connect(websocket=ws, username=username)
    while True:  # just to save socket connection 
        await ws.receive_text()

        
class ChessConnectionManager:
    """
    Chess game connection manager. Collects websockets to the game rooms.
    """
    def __init__(self):
        self.connections: dict[str, list] = {}

    async def connect(self, websocket, game_id: str) -> None:
        """Connect to the game."""
        if game_id in self.connections:
            if len(self.connections[game_id]) < 2:
                self.connections[game_id].append(websocket)
            else:
                await websocket.close()
        else:
            self.connections[game_id] = [websocket]

    async def broadcast(self, websocket, game_id: str, data: dict) -> None:
        """Send move of websocket to all sockets in the game excluding websocket."""
        for ws in self.connections[game_id]:
            if websocket != ws:
                await ws.send_json(data)


chess_connection_manager = ChessConnectionManager()


@router.websocket('/chess/{game_id}')
async def sock_chess(
        ws: WebSocket,
        game_id: str = Path(),
):
    """Endpoint for playing chess (changing moves)."""
    await ws.accept()
    await chess_connection_manager.connect(websocket=ws, game_id=game_id)
    while True:
        move_data = await ws.receive_json()
        await chess_connection_manager.broadcast(websocket=ws, game_id=game_id, data=move_data)
