from fastapi import FastAPI

from .middleware import AuthenticationMiddleware
from .token import encode_jwt_token


class LoginManager:
    def __init__(
            self,
            app: FastAPI,
            secret_key: str,
            algorithm: str,
            expire_minutes: int
    ):
        self.algorithm = algorithm
        self.secret_key = secret_key
        self.expire_minutes = expire_minutes
        self._app = app

        self._configurate_app()

    @property
    def app(self) -> FastAPI:
        return self._app

    def _configurate_app(self):
        self.app.add_middleware(
            AuthenticationMiddleware,
            secret_key=self.secret_key,
            expire_minutes=self.expire_minutes,
            algorithm=self.algorithm
        )

    def create_token(self, data) -> str:
        return encode_jwt_token(
            user_data=data,
            secret_key=self.secret_key,
            expire_minutes=self.expire_minutes,
            algorithm=self.algorithm
        )
