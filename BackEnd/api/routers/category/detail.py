from models.category import Category
from fastapi import APIRouter, Depends
from uuid import UUID
from models.user import User
from utils.auth import get_current_user


from utils.db import session

router = APIRouter()


@router.get("/category/{id}")
def id(id: UUID, current_user: User = Depends(get_current_user)):

    result = Category.query.filter(Category.id == id).first()

    return {"data": result}
