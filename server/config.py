import os
from socket import gethostbyname
from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_DRIVER: str
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DB_PORT: str
    DB_HOST: str

    SECRET_KEY: str
    EXPIRE_MINUTES: int
    ALGORITHM: str

    SUPERUSER_NAME: str
    SUPERUSER_PASSWORD: str
    SUPERUSER_EMAIL: str

    @property
    def db_url(self) -> str:
        addr = gethostbyname(self.DB_HOST)
        db_url = "{driver}://{user}:{password}@{addr}:{port}/{name}"
        return db_url.format(
            driver=self.DB_DRIVER,
            user=self.DB_USER,
            password=self.DB_PASSWORD,
            addr=addr,
            port=self.DB_PORT,
            name=self.DB_NAME
        )

    class Config:
        if os.getenv("TEST"):
            env_file = '.test.env'
        elif os.getenv("DOCKER"):
            env_file = ".env"
        else:
            env_file = '.dev.env'


def get_app_settings():
    return Settings()


def get_app_settings_by_keys(*args):
    settings = get_app_settings()
    for key in args:
        yield settings.__getattribute__(key)
