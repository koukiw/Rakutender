from schemas.event.id import Id
from models.event import Event
from fastapi import APIRouter, Depends


from utils.auth import auth_middle_ware

router = APIRouter()


@router.get('/event/{eventId}')
def id(eventId, isbool: bool = Depends(auth_middle_ware)):
  
  result = Event.query.filter(Event.id == eventId).all()

  return result
  