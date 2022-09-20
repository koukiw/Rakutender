from schemas.event.show import Show, Rules
from models.event import Event
from fastapi import APIRouter, Depends
from utils.db import session
from models.user import User
from utils.auth import get_current_user

router = APIRouter()


@router.post("/event/show")
def show(body: Show, current_user: User = Depends(get_current_user)):

    event = Event.query
    if body.rules == None:
        result = event.limit(body.limit).offset(body.fr).all()
        return {"data": result}

    if body.rules.startAt != None:
        event = event.filter(Event.start_at == body.rules.startAt)

    if body.rules.endAt != None:
        event = event.filter(Event.end_at == body.rules.endAt)

    if body.rules.limitUpper != None:
        event = event.filter(Event.limit <= body.rules.limitUpper)

    if body.rules.limitUnder != None:
        event = event.filter(Event.limit >= body.rules.limitUnder)

    if body.rules.categoryId != None:
        event = event.filter(Event.category_id == body.rules.categoryId)

    result = event.limit(body.limit).offset(body.fr).all()

    return {"data": result}
