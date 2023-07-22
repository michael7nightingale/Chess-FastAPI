from datetime import datetime

from sqlalchemy import update

from .base import BaseRepository
from infrastructure.db.models import Game


class GameRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(model=Game, session=session)

    def finish(self, game_id: str, winner: str):
        query = update(self.model).where(self.model.id == game_id).values(
            winner=winner,
            time_finish=datetime.now()
        )
        self.session.execute(query)
        self.commit()
