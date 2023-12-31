from fastapi import FastAPI, APIRouter
from fastapi_authtools import AuthManager

from db import create_engine_, create_sessionmaker
from db.events import create_superuser, custom_user_getter
from api.routes import __routers__
from config import get_app_settings


class Server:
    __slots__ = ("_app", "_settings", "_engine", "_pool")

    def __init__(self, app: FastAPI):
        self._settings = get_app_settings()
        self._app: FastAPI = app
        self._configurate_db()
        self._configurate_auth()
        self._configurate_routes(*__routers__)

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
            algorithm=self.settings.ALGORITHM,
            user_getter=custom_user_getter
        )

    def _on_startup(self):
        self.app.state.pool = self.pool

    def _on_shutdown(self):
        self.engine.dispose()

    def _configurate_db(self) -> None:
        self._engine = create_engine_(self.settings.db_url)
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
