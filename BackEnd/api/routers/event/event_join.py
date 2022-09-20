from schemas.event.eventJoin import EventJoin
from fastapi import APIRouter, Depends, status
from models.participant import Participant
from uuid import UUID
from utils.db import session
from fastapi.responses import JSONResponse
from models.user import User
from utils.auth import get_current_user


router = APIRouter()


@router.post("/event/{id}/join")
def event_join(
    id: UUID, body: EventJoin, current_user: User = Depends(get_current_user)
):
    participant = Participant()
    participant.user_id = current_user.id
    participant.event_id = id
    participant.deleted_at = body.deleted_at

    session.add(participant)
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

    # return {"status": "success!"}
