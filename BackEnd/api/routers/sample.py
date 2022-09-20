from models.user import User
from utils.auth import get_current_user
from schemas.sample import Rakuten
from fastapi import APIRouter, Depends


router = APIRouter()


@router.get(
    "/current-user",
)
def get_current_user(current_user: User = Depends(get_current_user)):
    return {"data": current_user}
