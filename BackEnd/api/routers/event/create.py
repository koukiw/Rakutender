from schemas.event.create import Create
from models.event import Event
from models.user import User
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from utils.db import session
from models.user import User
from utils.auth import get_current_user


router = APIRouter()


@router.post("/event/create")
def event_create(body: Create, current_user: User = Depends(get_current_user)):
    event = Event()
    event.name = body.name
    event.category_id = body.categoryId
    event.limit = body.limit
    event.start_at = body.startAt
    event.end_at = body.endAt
    event.created_user_id = current_user.id

    session.add(event)
    try:
        session.commit()
    except:
        session.rollback()
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, content={"status": "failed"}
        )

    return JSONResponse(
        status_code=status.HTTP_201_CREATED, content={"status": "success"}
    )
