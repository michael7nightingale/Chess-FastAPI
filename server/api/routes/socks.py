from fastapi import WebSocket, APIRouter, Path, Depends
import asyncio
import json
from random import choice, shuffle

from package.chess import Chess
from api.dependencies import get_repository, get_socket_repository
from infrastructure.db.repositories import UserRepository, GameRepository
from infrastructure.redis_ import redis_session


router = APIRouter(
    prefix="/ws"
)
player_colors = {"white", "black"}


class WaitConnectionManager:
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


@router.websocket("/wait-player")
async def wait_for_the_plater(
    ws: WebSocket,

):
    await ws.accept()
    username = await ws.receive_text()
    await wait_connection_manager.connect(websocket=ws, username=username)
    while True:
        await ws.receive_text()

        
class ChessConnectionManager:
    def __init__(self):
        self.connections: dict[str, list] = {}

    async def connect(self, websocket, game_id: str) -> None:
        # await websocket.accept()
        if game_id in self.connections:
            if len(self.connections[game_id]) < 2:
                self.connections[game_id].append(websocket)
            else:
                await websocket.close()
        else:
            self.connections[game_id] = [websocket]

    async def broadcast(self, game_id: str, data: dict) -> None:
        for ws in self.connections[game_id]:
            await ws.send_json(data)


chess_connection_manager = ChessConnectionManager()


@router.websocket('/chess/{game_id}')
async def sock_chess(
        ws: WebSocket,
        game_id: str = Path(),
):
    await ws.accept()
    await chess_connection_manager.connect(websocket=ws, game_id=game_id)
    while True:
        move_data = await ws.receive_json()
        await chess_connection_manager.broadcast(game_id=game_id, data=move_data)
