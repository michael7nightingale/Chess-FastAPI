from fastapi import Depends
from config import get_app_settings
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from starlette.requests import Request

from typing import Type

from db.repositories import UserRepository, GameRepository
from db.repositories.base import BaseRepository


def _get_pool(request: Request):
    """Session maker pool is placed in app`s state on app`s startapp"""
    return request.app.state.pool


def _get_session(pool=Depends(_get_pool)):
    """Save get and close the session"""
    with pool() as session:
        yield session


def _get_socket_pool(func):
    engine = create_engine(get_app_settings().db_url)
    pool = sessionmaker(bind=engine)

    def inner(pool_=pool, *args, **kwargs):
        return func(pool_=pool_, *args, **kwargs)

    return inner


@_get_socket_pool
def _get_socket_session(pool_: sessionmaker):
    with pool_() as session:
        yield session


def get_socket_repository(repo_type: Type[BaseRepository]):
    """Get repository instance after getting the session."""

    def _get_repo(session=_get_socket_session) -> BaseRepository:
        return repo_type(next(session()))

    return _get_repo


def get_repository(repo_type: Type[BaseRepository]):
    """Get repository instance after getting the session."""
    def _get_repo(session=Depends(_get_session)) -> BaseRepository:
        return repo_type(session)
    return _get_repo


get_user_repository = get_repository(UserRepository)
get_game_repository = get_repository(GameRepository)
