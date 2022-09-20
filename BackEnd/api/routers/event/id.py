from models.event import Event
from fastapi import APIRouter, Depends
from models.user import User
from utils.auth import get_current_user

from utils.db import session

router = APIRouter()


@router.get("/event/{id}")
def id(id, current_user: User = Depends(get_current_user)):

    # event = Event()
    # event.name = "カテゴリ"
    # event.category_id = "05be752aa2484d0098d559b9cefebc65"
    # event.created_user_id = "e8c342a292d94ad3ac7b01ba46dc878d"

    # user = User()
    # user.username = "aaa"

    # session.add(event)
    # session.commit()

    result = Event.query.filter(Event.id == id)
    result = result.all()
    return {"data": result}
