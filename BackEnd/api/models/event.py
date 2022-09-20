from uuid import uuid4
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy_utils import UUIDType
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from models.participant import Participant
from utils.db import Base


class Event(Base):
    __tablename__ = "events"
    __table_args__ = {"comment": "イベント"}

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid4, comment="ID")
    name = Column(String(length=100), nullable=False, comment="イベント名")
    category_id = Column(
        ForeignKey("categories.id"),
        nullable=False,
        comment="イベントカテゴリ",
    )
    limit = Column(Integer, nullable=True, comment="参加上限人数")
    start_at = Column(DateTime, nullable=True, comment="イベント開始日時")
    end_at = Column(DateTime, nullable=True, comment="イベント終了日時")
    created_user_id = Column(ForeignKey("users.id"), nullable=False, comment="作成者")
    created_at = Column(
        DateTime, nullable=False, server_default=func.now(), comment="データ登録日"
    )
    updated_at = Column(
        DateTime, nullable=True, server_onupdate=func.now(), comment="データ更新日"
    )
    deleted_at = Column(DateTime, nullable=True, comment="論理削除されたかどうか")
    users = relationship(
        "User",
        secondary=Participant.__tablename__,
        back_populates="events",
    )
