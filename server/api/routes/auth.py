from fastapi import APIRouter, Body, Depends, Request
from fastapi_authtools.exceptions import raise_credentials_error

from api.dependencies.auth import get_superuser
from api.dependencies.database import get_repository
from db.repositories import UserRepository
from db.models import User
from schemas.user import UserShow, UserRegister, UserLogin


auth_router = APIRouter(prefix='/auth', tags=['Auth'])


@auth_router.get("/all")
async def get_all_users(user_repo: UserRepository = Depends(get_repository(UserRepository)),
                        superuser: UserShow = Depends(get_superuser)):
    """Get list of all registered users. Only for superuser."""
    users: list[User] = user_repo.all()
    return [u.as_dict() for u in users]


@auth_router.post("/register", status_code=201)
async def register_user(user_repo: UserRepository = Depends(get_repository(UserRepository)),
                        user_schema: UserRegister = Body()) -> UserShow | dict:
    """Register user endpoint. All schema data is needed."""
    registered_user: User = user_repo.create(user_schema)
    if registered_user is None:
        return {"detail": "Username already exists."}
    return UserShow(**registered_user.as_dict())


@auth_router.post("/token")
async def get_token(
        request: Request,
        user_data: UserLogin = Body(),
        user_repo: UserRepository = Depends(get_repository(UserRepository))
):
    """Get auth token by login data (username, password) in request Body"""
    user = user_repo.login(user_data)
    if user is None:
        raise_credentials_error()
    return {"access_token": request.app.state.auth_manager.create_token(UserShow(**user.as_dict()))}


@auth_router.get("/me")
async def get_me(request: Request):
    """Get auth token by login data (username, password) in request Body"""
    return request.user.data
