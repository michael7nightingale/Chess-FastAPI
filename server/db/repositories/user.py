from sqlalchemy.orm import Session

from db.models import User
from db.repositories.base import BaseRepository
from schemas.user import UserLogin, UserRegister

from package.hasher import hash_password, verify_password


class UserRepository(BaseRepository):
    """
    Repository for User model
    """
    def __init__(self, session: Session):
        super().__init__(User, session)   # note: model is prescribed

    def create(self, user_schema: UserRegister):
        """Register method"""
        user_schema.password = hash_password(user_schema.password)
        new_user = super().create(**user_schema.dict())
        return new_user

    def login(self, user_schema: UserLogin) -> User | None:
        user = self.get_by(username=user_schema.username)
        if verify_password(user_schema.password, user.password):
            return user
        else:
            return None
