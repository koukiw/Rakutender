from models.event import Participant, Event
from fastapi import APIRouter, Depends
from uuid import UUID
from models.user import User
from utils.auth import get_current_user
from utils.db import session

router = APIRouter()


@router.get("/event/{id}/participants")
def id(id: UUID, current_user: User = Depends(get_current_user)):
    results = Participant.query.filter(Participant.event_id == id).all()
    participants_list = [
        User.query.filter(User.id == result.user_id).first() for result in results
    ]
    return {"data": participants_list}
