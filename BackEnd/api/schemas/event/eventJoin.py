from typing import Optional

# from xmlrpc.client import DateTime
from pydantic import BaseModel
import datetime
from uuid import UUID


class EventJoin(BaseModel):
    deleted_at: Optional[datetime.datetime]
