from sqlalchemy.orm import Session
from sqlalchemy import delete, update, select
from sqlalchemy.exc import IntegrityError
from typing import TypeVar

from infrastructure.db.models.base import BaseAlchemyModel


Model = TypeVar("Model", bound=BaseAlchemyModel)


class BaseRepository:
    """
    Base repository pattern class
    """
    def __init__(self, model: type[Model], session: Session):
        self._model = model
        self._session = session

    def create(self, **kwargs) -> Model:
        """Create new object in the table"""
        try:
            new_obj = self._model(
                **kwargs
            )
            self.save(new_obj)
            return new_obj
        except IntegrityError:
            return None

    def save(self, obj):
        """Comfortably save object"""
        self.add(obj)
        self.commit()

    def get(self, id_: int) -> Model:
        """Get object by pk (id)"""
        query = select(self._model).where(self._model.id == id_)
        return self._session.execute(query).scalar_one_or_none()

    def get_by(self, **kwargs) -> Model:
        """Filter all objects by kwargs"""
        query = select(self._model).filter_by(**kwargs)
        return self._session.execute(query).scalar_one_or_none()

    def filter(self, **kwargs) -> list[Model]:
        """Filter all objects by kwargs"""
        query = select(self._model).filter_by(**kwargs)
        return self._session.execute(query).scalars().all()

    def all(self) -> list[Model]:
        """Get all objects from the table"""
        query = select(self._model)
        return self._session.execute(query).scalars().all()

    def update(self, id_, **kwargs):
        """Update object by pk (id) with values kwargs"""
        query = update(self._model).where(self._model.id == id_).values(**kwargs)
        self._session.execute(query)
        self.commit()

    def delete(self, id_) -> None:
        """Delete object by pk (id)"""
        query = delete(self._model).where(self._model.id == id_)
        self._session.execute(query)
        self.commit()

    def clear(self) -> None:
        """Delete all objects from the table."""
        query = delete(self._model)
        self._session.execute(query)
        self.commit()

    def commit(self):
        """Comfortably commit changes"""
        self._session.commit()

    def add(self, obj):
        """Comfortably add object"""
        self._session.add(obj)


class SlugGetMixin:
    """
    Mixin for slug-getter can be useful
    """
    _session: Session
    _model: Model

    def get(self, slug: str):
        """Get on unique slug"""
        query = select(self._model).where(self._model.slug == slug)
        return self._session.execute(query).scalar()
