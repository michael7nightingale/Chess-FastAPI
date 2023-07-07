from fastapi import WebSocket, APIRouter, Path, Depends
from package.chess import Chess
from api.dependencies import get_repository
from infrastructure.db.repositories import UserRepository


router = APIRouter(
    prefix="/websocket"
)


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

