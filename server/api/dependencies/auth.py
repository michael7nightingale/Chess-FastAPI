from fastapi import Depends, Body, Request
from starlette.exceptions import HTTPException

from infrastructure.db.repositories import UserRepository
from api.dependencies.database import get_repository
from api.responses import AuthDetail
from schemas.user import UserLogin


async def login_current_user(user_repo: UserRepository = Depends(get_repository(UserRepository)),
                             user_form: UserLogin = Body()):    # OAuth2PasswordRequestForm if needed
    """Dependency for getting user by login data from DB."""
    try:
        user = user_repo.login(user_form)
        return user
    except AttributeError:
        raise HTTPException(status_code=403, detail=AuthDetail.login_data_error.value)


async def get_superuser(request: Request):
    """Checks if current user is superuser"""
    if not request.user.data.get('is_superuser'):
        raise HTTPException(status_code=403, detail=AuthDetail.no_permissions.value)
