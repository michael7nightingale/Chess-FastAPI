from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext
from uuid import uuid4

from config import get_app_settings


crypto_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def decode_access_token(token) -> dict | None:
    try:
        settings = get_app_settings()
        return jwt.decode(
            token=token,
            key=settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
    except JWTError:
        return


def create_uuid():
    return str(uuid4())


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    settings = get_app_settings()
    to_encode.update(exp=datetime.utcnow() + timedelta(minutes=settings.EXPIRE_MINUTES))
    return jwt.encode(
        claims=data,
        key=settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )
