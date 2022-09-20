from typing import Optional
#from xmlrpc.client import DateTime
from pydantic import BaseModel
import datetime
from uuid import UUID


class Rules(BaseModel):
    startAt: Optional[datetime.datetime]
    endAt: Optional[datetime.datetime]
    limitUpper: Optional[int]
    limitUnder: Optional[int]
    categoryId: Optional[str]


class Order(BaseModel):
    """
    未実装
    flag: Optional[bool[3]]
    updown: optional[bool]

    startAt: Optional[datetime.datetime]
    limit: Optional[int]
    createdAt: datetime.datetime

    up->True down->False
    """

class Show(BaseModel):
    """
    id: int
    name: str
    categoryId: UUID
    limit: Optional[int]
    startAt: Optional[datetime.datetime]
    endAt: Optional[datetime.datetime]
    """
    rules: Optional[Rules]
    page: int = 1
