from fastapi import Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from utils.auth import (
    get_current_user,
    get_current_user_with_refresh_token,
    create_tokens,
    authenticate,
)

from models.user import User

router = APIRouter()


@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user = authenticate(form.username, form.password)
    return create_tokens(str(user.id))


@router.get("/refresh_token/")
async def refresh_token(
    current_user: User = Depends(get_current_user_with_refresh_token),
):
    return create_tokens(current_user.id)


@router.get("/users/me/")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
