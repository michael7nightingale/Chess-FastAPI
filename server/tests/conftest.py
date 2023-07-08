import os
import pytest
import asyncio
import pytest_asyncio
from fastapi import FastAPI
from httpx import AsyncClient
import sys
sys.path.append(os.getcwd())
print(sys.path)
from configuration.server import Server
from infrastructure.db import Base
from api.routes import __routes__


pytest.mark.asyncio
os.environ['TEST'] = "1"


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="function")
async def get_application():
    os.environ['TEST'] = "1"
    server = Server(FastAPI())
    Base.metadata.create_all(bind=server._engine)
    yield server.app
    Base.metadata.drop_all(bind=server._engine)


@pytest_asyncio.fixture(scope="function")
async def client(get_application):
    async with AsyncClient(app=get_application) as cl:
        yield cl


def url_for(router):
    def inner(name, **params):
        return router.url_for(name, **params)
    return inner


sock_router, auth_router = __routes__

get_sock_url = url_for(sock_router)
get_auth_url = url_for(auth_router)
