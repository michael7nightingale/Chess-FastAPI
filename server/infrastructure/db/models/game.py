from sqlalchemy import String, Column, ForeignKey, DateTime, func
from uuid import uuid4

from infrastructure.db import Base, TableMixin


class Game(Base, TableMixin):
    __tablename__ = "games"

    id = Column(String(100), primary_key=True, default=lambda: str(uuid4()))
    black_user = Column(String(100), ForeignKey("users.id"))
    white_user = Column(String(100), ForeignKey("users.id"))
    winner = Column(String(100), ForeignKey("users.id"), nullable=True)
    time_start = Column(DateTime, server_default=func.now())
    time_finish = Column(DateTime, nullable=True)
