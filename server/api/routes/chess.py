from fastapi import APIRouter, Depends

from api.dependencies import get_current_user, get_repository


router = APIRouter(
    prefix="/games"
)


@router.post("/create")
async def create_game(
        user=Depends(get_current_user),
        game_repo=get_repository()
):
    ...
