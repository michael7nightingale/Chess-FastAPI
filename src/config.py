import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_URI: str = f"postgresql://postgres:password@localhost/chess"

    SECRET_KEY: str
    EXPIRE_MINUTES = 60 * 24
    ALGORITHM = "HS256"

    SUPERUSER_NAME: str
    SUPERUSER_PASSWORD: str
    SUPERUSER_EMAIL: str

    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379

    class Config:
        if os.getenv("TEST"):
            env_file = '../.test.env'
        elif os.getenv("PROD"):
            env_file = "../.prod.env"
        else:
            env_file = '../.env'


def get_app_settings():
    return Settings()


def get_app_settings_by_keys(*args):
    settings = get_app_settings()
    for key in args:
        yield settings.__getattribute__(name=key)
