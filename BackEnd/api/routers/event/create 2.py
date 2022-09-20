from schemas.event.create import Create
from models.event import Event
from fastapi import APIRouter, Depends


from utils.auth import auth_middle_ware

router = APIRouter()


@router.post('/event/create')
def event_create(body:Create, isbool: bool = Depends(auth_middle_ware)):
  event = Event()
  event.name = body.name
  event.category_id = body.categoryId
  event.limit = body.limit
  event.start_at = body.startAt
  event.end_at = body.endAt

  Event.add(event)
  Event.commit()

  return { "status": "success"}
