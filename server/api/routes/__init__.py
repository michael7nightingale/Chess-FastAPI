from .auth import auth_router
from .chess import chess_router

__routes__ = (chess_router, auth_router)
