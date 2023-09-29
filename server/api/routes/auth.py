from fastapi import APIRouter, Body, Depends, Request
from fastapi_authtools import login_required
from fastapi_authtools.exceptions import raise_invalid_credentials

from api.dependencies.auth import get_superuser
from api.dependencies.database import get_user_repository
from db.repositories import UserRepository
from db.models import User
from schemas.user import UserShow, UserRegister, UserLogin


router = APIRouter(prefix='/auth', tags=['Auth'])


@router.get("/all")
async def get_all_users(
        user_repo: UserRepository = Depends(get_user_repository),
        superuser: UserShow = Depends(get_superuser)
):
    """Get list of all registered users. Only for superuser."""
    users: list[User] = user_repo.all()
    return [u.as_dict() for u in users]


@router.post("/register", status_code=201)
async def register_user(user_repo: UserRepository = Depends(get_user_repository),
                        user_schema: UserRegister = Body()) -> UserShow | dict:
    """Register user endpoint. All schema data is needed."""
    registered_user: User = user_repo.create(user_schema)
    if registered_user is None:
        return {"detail": "Username already exists."}
    return UserShow(**registered_user.as_dict())


@router.post("/token")
async def get_token(
        request: Request,
        user_data: UserLogin = Body(),
        user_repo: UserRepository = Depends(get_user_repository)
):
    """Get auth token by login data (username, password) in request Body"""
    user = user_repo.login(user_data)
    if user is None:
        raise_invalid_credentials()
    return {"access_token": request.app.state.auth_manager.create_token(UserShow(**user.as_dict()))}


@router.get("/me")
@login_required
async def get_me(request: Request):
    return request.user
