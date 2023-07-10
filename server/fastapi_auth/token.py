from datetime import datetime, timedelta
import typing

from jose import JWTError, jwt
from pydantic import BaseModel, ValidationError


def encode_jwt_token(
        user_data: dict | BaseModel,
        secret_key: str,
        algorithm: str,
        expire_minutes: int
) -> str:
    if isinstance(user_data, BaseModel):
        user_data = user_data.model_dump()
    user_data.update(exp=datetime.now() + timedelta(minutes=expire_minutes))
    token = jwt.encode(
        user_data,
        key=secret_key,
        algorithm=algorithm
    )
    return token


def decode_jwt_token(
        token: str,
        algorithm: str,
        secret_key: str,
        out_model: typing.Type[BaseModel] | None = None
) -> dict | BaseModel | None:
    try:
        data = jwt.decode(
            token=token,
            key=secret_key,
            algorithms=[algorithm]
        )
        return data if out_model is None else out_model(**data)

    except (JWTError, ValidationError):
        return None
