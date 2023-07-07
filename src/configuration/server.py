from fastapi import FastAPI, APIRouter

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
        self._configurate_routes(*__routes__)

    @property
    def app(self) -> FastAPI:
        return self._app

    def _configurate_routes(self, *routers: APIRouter) -> None:
        for r in routers:
            self._app.include_router(r)

    def _on_startup(self):
        self._app.state.pool = self._pool

    def _on_shutdown(self):
        self._engine.dispose()

    def _configurate_db(self) -> None:
        self._engine = create_engine_(self._settings.DB_URI)
        self._pool = create_sessionmaker(self._engine)
        create_superuser(self._pool)
        self._app.add_event_handler(
            event_type="startup",
            func=lambda: self._on_startup()
        )

        self._app.add_event_handler(
            event_type="shutdown",
            func=lambda: self._on_shutdown()
        )
