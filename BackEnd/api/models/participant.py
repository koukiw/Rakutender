from uuid import uuid4
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy_utils import UUIDType
from sqlalchemy.sql import func

from utils.db import Base


class Participant(Base):
    __tablename__ = "participants"
    __table_args__ = {"comment": "参加者"}

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid4, comment="ID")
    user_id = Column(ForeignKey("users.id"), nullable=False, comment="イベント名")
    event_id = Column(ForeignKey("events.id"), nullable=False, comment="イベントカテゴリ")
    created_at = Column(
        DateTime, nullable=False, server_default=func.now(), comment="データ登録日"
    )
    updated_at = Column(
        DateTime, nullable=True, server_onupdate=func.now(), comment="データ更新日"
    )
    deleted_at = Column(DateTime, nullable=True, comment="論理削除されたかどうか")
