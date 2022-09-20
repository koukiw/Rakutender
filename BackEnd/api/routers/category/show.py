from fastapi import APIRouter, Depends
from uuid import UUID
from typing import List
from models.category import Category
from models.user import User
from utils.auth import get_current_user


router = APIRouter()


@router.get("/category/show")
def category_show(current_user: User = Depends(get_current_user)):
    result = Category.query.all()

    return {"data": result}
