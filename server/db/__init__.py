from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, declarative_base


def create_sessionmaker(engine: Engine) -> sessionmaker:
    session = sessionmaker(
        bind=engine,
        autoflush=False,
        expire_on_commit=False,
    )
    return session


def create_engine_(dns: str) -> Engine:
    engine = create_engine(url=dns)
    return engine


Base = declarative_base()


class TableMixin:
    """For getting dict object of the model."""

    def as_dict(self):
        return {i.name: getattr(self, i.name) for i in self.__table__.columns}
