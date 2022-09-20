from typing import Optional
#from xmlrpc.client import DateTime
from pydantic import BaseModel
import datetime
from uuid import UUID


class Create(BaseModel):
  id: int
  name: str
  categoryId: UUID
  limit: Optional[int]
  startAt: Optional[datetime.datetime]
  endAt: Optional[datetime.datetime]
