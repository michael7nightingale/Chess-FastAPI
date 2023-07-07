from typing import Type

from fastapi import Depends
from starlette.requests import Request

from infrastructure.db.repositories.base import BaseRepository


def _get_pool(request: Request):
    """Session maker pool is placed in app`s state on app`s startapp"""
    return request.app.state.pool


def _get_session(pool=Depends(_get_pool)):
    """Save get and close the session"""
    with pool() as session:
        yield session


def get_repository(repo_type: Type[BaseRepository]):
    """Get repository instance after getting the session."""
    def _get_repo(session=Depends(_get_session)) -> BaseRepository:
        return repo_type(session)
    return _get_repo
