from models.event import Participant, Event
from fastapi import APIRouter, Depends
from uuid import UUID
from models.user import User
from utils.auth import get_current_user
from utils.db import session

router = APIRouter()


@router.get("/my-event")
def id(current_user: User = Depends(get_current_user)):
    results = Participant.query.filter(Participant.user_id == current_user.id).all()
    list = []
    event_list = []
    for result in results:
        list.append(result.event_id)
        event_list.append(Event.query.filter(Event.id == result.event_id).first())
    return {"data": event_list}
