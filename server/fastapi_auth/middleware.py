from fastapi import FastAPI
from starlette.middleware import authentication
from starlette.requests import Request
from starlette.responses import JSONResponse
import typing

from .backend import AuthenticationBackend


def AuthenticationMiddleware(
        app: FastAPI,
        secret_key: str,
        algorithm: str,
        expire_minutes: int,
        auth_error_handler: typing.Callable[[Request, authentication.AuthenticationError], JSONResponse] = None,
        excluded_urls: typing.List[str] = None,
) -> authentication.AuthenticationMiddleware:
    return authentication.AuthenticationMiddleware(
        app=app,
        backend=AuthenticationBackend(
            secret_key=secret_key,
            algorithm=algorithm,
            expire_minutes=expire_minutes,
            excluded_urls=excluded_urls
        ),
        on_error=auth_error_handler
    )


