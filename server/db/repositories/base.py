from sqlalchemy.orm import Session
from sqlalchemy import delete, update, select
from sqlalchemy.exc import IntegrityError
from typing import TypeVar

from db.models.base import BaseAlchemyModel


Model = TypeVar("Model", bound=BaseAlchemyModel)


class BaseRepository:
    """
    Base repository pattern class
    """
    def __init__(self, model: type[Model], session: Session):
        self._model = model
        self._session = session

    @property
    def model(self):
        return self._model

    @property
    def session(self) -> Session:
        return self._session

    def create(self, **kwargs) -> Model | None:
        """Create new object in the table"""
        try:
            new_obj = self.model(
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

    def get(self, *args, **kwargs) -> Model:
        """Get object by pk (id)"""
        if len(args) != 0:
            if len(args) == 1:
                kwargs.update(id=args[0])
            else:
                raise ValueError("1 argument id expected")
        expected = (getattr(self.model, k) == v for k, v in kwargs.items())
        query = select(self.model).where(*expected).limit(1)
        return self.session.execute(query).scalar_one_or_none()

    def get_by(self, **kwargs) -> Model:
        """Filter all objects by kwargs"""
        query = select(self.model).filter_by(**kwargs)
        return self.session.execute(query).scalar_one_or_none()

    def filter(self, **kwargs) -> list[Model]:
        """Filter all objects by kwargs"""
        query = select(self.model).filter_by(**kwargs)
        return self.session.execute(query).scalars().all()

    def all(self) -> list[Model]:
        """Get all objects from the table"""
        query = select(self.model)
        return self.session.execute(query).scalars().all()

    def update(self, id_, **kwargs):
        """Update object by pk (id) with values kwargs"""
        query = update(self.model).where(self.model.id == id_).values(**kwargs)
        self.session.execute(query)
        self.commit()

    def delete(self, id_) -> None:
        """Delete object by pk (id)"""
        query = delete(self.model).where(self.model.id == id_)
        self.session.execute(query)
        self.commit()

    def clear(self) -> None:
        """Delete all objects from the table."""
        query = delete(self.model)
        self.session.execute(query)
        self.commit()

    def commit(self):
        """Comfortably commit changes"""
        self.session.commit()

    def add(self, obj):
        """Comfortably add object"""
        self.session.add(obj)


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
