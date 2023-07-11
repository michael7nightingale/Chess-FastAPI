import asyncio

from fastapi import WebSocket, APIRouter, Path, Depends
from random import choice, shuffle

from package.chess import Chess
from api.dependencies import get_repository, get_socket_repository
from infrastructure.db.repositories import UserRepository, GameRepository
from infrastructure.redis_ import redis_session


router = APIRouter(
    prefix="/ws"
)
player_colors = {"white", "color"}


class ChessSocket:
    __slots__ = ("sock", "user", "game_id")

    def __init__(self, sock: WebSocket, game_id: str, user):
        self.sock = sock
        self.game_id = game_id
        self.user = user

    async def accept(self) -> None:
        await self.sock.accept()

    async def listen_forever(self) -> None:
        while True:
            data = await self.sock.receive_text()
            cell_id = data
            chessboard = Chess()

            to_move: str | None = chessboard.move(cell_id)
            if to_move is None:
                pass
            else:
                await self.sock.send_text(f"{to_move} {cell_id}")


@router.websocket("/wait-player")
async def wait_for_the_plater(
    ws: WebSocket,

):
    game_repo: GameRepository = get_socket_repository(GameRepository)()
    user_repo: UserRepository = get_socket_repository(UserRepository)()
    await ws.accept()
    username = await ws.receive_text()
    while True:
        usernames = redis_session.keys("*")
        if len(usernames):
            enemy_username = choice(usernames).decode()
            if enemy_username != username:
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
                redis_session.delete(enemy_username)
                # redis_session.sync()
                await ws.send_json(game_data)
                break
        else:
            redis_session.set(username, 1)

        await asyncio.sleep(0)


@router.websocket('/chessboard/{game_id}/{user_id}')
async def sock_chess(
        sock: WebSocket,
        game_id: str = Path(),
        user_id: str | int = Path(),
        user_repo: UserRepository = Depends(get_repository(UserRepository))
):
    chess_socket = ChessSocket(
        sock=sock,
        game_id=game_id,
        user=user_repo.get(user_id)
    )
    await chess_socket.accept()
    await chess_socket.listen_forever()

