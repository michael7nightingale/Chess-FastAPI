from fastapi import FastAPI
from configuration.server import Server


def create_app() -> FastAPI:
    app = FastAPI()
    return Server(app).app


app = create_app()
