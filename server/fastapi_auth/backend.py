from starlette import authentication
from starlette.datastructures import Headers
from starlette.requests import HTTPConnection
from pydantic import typing, BaseModel
import typing

from .token import decode_jwt_token
from .user import FastAPIUser


class AuthenticationBackend(authentication.AuthenticationBackend):
    def __init__(
            self,
            secret_key: str,
            algorithm: str,
            expire_minutes: int,
            excluded_urls=None
    ):
        self.secret_key = secret_key
        self.algorithm = algorithm
        self.expire_minutes = expire_minutes
        self.excluded_urls = [] if excluded_urls is None else excluded_urls

    def verify_token(self, headers: dict | Headers):
        token = headers.get("authorization") or headers.get("Authorization")
        scopes = []
        if token is None:
            return scopes, None

        token = token.split()[-1]
        user_data = decode_jwt_token(
            token=token,
            secret_key=self.secret_key,
            algorithm=self.algorithm
        )
        if user_data is None:
            return scopes, None

        user = FastAPIUser(**user_data.model_dump()) if isinstance(user_data, BaseModel) else FastAPIUser(**user_data)
        return scopes, user

    async def authenticate(
        self, conn: HTTPConnection
    ) -> typing.Optional[typing.Tuple[authentication.AuthCredentials, authentication.BaseUser | None]]:
        if conn.url.path in self.excluded_urls:
            return authentication.AuthCredentials([]), None

        response = self.verify_token(conn.headers)
        if isinstance(response, typing.Awaitable):
            response = await response

        scopes, user = response

        return authentication.AuthCredentials(scopes=scopes), user
