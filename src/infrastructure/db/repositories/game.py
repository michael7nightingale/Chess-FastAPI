from .base import BaseRepository
from infrastructure.db.models import Game


class GameRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(model=Game, session=session)
