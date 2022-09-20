from typing import Optional

# from xmlrpc.client import DateTime
from pydantic import BaseModel
import datetime
from uuid import UUID


class Rules(BaseModel):
    startAt: Optional[datetime.datetime]
    endAt: Optional[datetime.datetime]
    limitUpper: Optional[int]
    limitUnder: Optional[int]
    categoryId: Optional[UUID]


class Show(BaseModel):
    """
    id: int
    name: str
    categoryId: UUID
    limit: Optional[int]
    startAt: Optional[datetime.datetime]
    endAt: Optional[datetime.datetime]
    """

    rules: Rules = None
    fr: int = 0
    limit: int = 10
