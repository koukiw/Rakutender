from typing import Optional
# from xmlrpc.client import DateTime
from pydantic import BaseModel
import datetime
from uuid import UUID

class EventJoin(BaseModel):
  id: UUID
  user_id: int
  event_id:int
  created_at:datetime.datetime
  updated_at:Optional[datetime.datetime]
  deleted_at:Optional[datetime.datetime]
