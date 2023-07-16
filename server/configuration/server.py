import socket

from fastapi import FastAPI, APIRouter
from fastapi_authtools import AuthManager

from infrastructure.db import create_engine_, create_sessionmaker
from infrastructure.db.utils import create_superuser
from api.routes import __routes__
from config import get_app_settings


class Server:
    __slots__ = ("_app", "_settings", "_engine", "_pool")

    def __init__(self, app: FastAPI):
        self._settings = get_app_settings()
        self._app: FastAPI = app
        self._configurate_db()
        self._configurate_auth()
        self._configurate_routes(*__routes__)

    @property
    def app(self) -> FastAPI:
        return self._app

    @property
    def engine(self):
        return self._engine

    @property
    def pool(self):
        return self._pool

    @property
    def settings(self):
        return self._settings

    def _configurate_routes(self, *routers: APIRouter) -> None:
        for r in routers:
            self._app.include_router(r)

    def _configurate_auth(self):
        self.app.state.auth_manager = AuthManager(
            app=self.app,
            secret_key=self.settings.SECRET_KEY,
            expire_minutes=self.settings.EXPIRE_MINUTES,
            algorithm=self.settings.ALGORITHM
        )

    def _on_startup(self):
        self.app.state.pool = self.pool

    def _on_shutdown(self):
        self.engine.dispose()

    def _configurate_db(self) -> None:
        addr = socket.gethostbyname(self.settings.DB_HOST)
        user = self.settings.DB_USER
        password = self.settings.DB_PASSWORD
        port = self.settings.DB_PORT
        name = self.settings.DB_NAME
        db_uri = f"postgresql://{user}:{password}@{addr}:{port}/{name}"
        self._engine = create_engine_(db_uri)
        self._pool = create_sessionmaker(self.engine)

        create_superuser(self._pool)
        self._app.add_event_handler(
            event_type="startup",
            func=lambda: self._on_startup()
        )

        self._app.add_event_handler(
            event_type="shutdown",
            func=lambda: self._on_shutdown()
        )
