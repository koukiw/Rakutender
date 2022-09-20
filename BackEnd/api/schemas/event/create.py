from typing import Optional
#from xmlrpc.client import DateTime
from pydantic import BaseModel
import datetime
from uuid import UUID


class Create(BaseModel):
  name: str
  categoryId: UUID
  createdUserId :UUID
  limit: Optional[int]
  startAt: Optional[datetime.datetime]
  endAt: Optional[datetime.datetime]
