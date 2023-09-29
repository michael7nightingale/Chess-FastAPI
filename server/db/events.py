from db.models.user import User
from package.hasher import hash_password
from sqlalchemy.exc import IntegrityError

from config import get_app_settings
from . import create_engine_, create_sessionmaker
from db.repositories import UserRepository


def create_superuser(pool):
    with pool() as session:
        settings = get_app_settings()
        try:
            superuser = User(
                username=settings.SUPERUSER_NAME,
                password=hash_password(settings.SUPERUSER_PASSWORD),
                first_name='Michael',
                last_name='Nightingale',
                email=settings.SUPERUSER_EMAIL,
                is_superuser=True,
                is_staff=True
            )
            session.add(superuser)
            session.commit()
        except IntegrityError:  # superuser exists
            pass


def custom_user_getter(**kwargs) -> User | None:
    username = kwargs.get("username")
    pool = create_sessionmaker(create_engine_(get_app_settings().db_url))
    with pool() as session:
        user_repo = UserRepository(session)
        user = user_repo.get(username=username)
        return user
