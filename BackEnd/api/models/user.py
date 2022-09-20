from http import server
from uuid import uuid4
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text
from sqlalchemy_utils import UUIDType
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from models.participant import Participant
from utils.db import Base


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"comment": "ユーザー"}

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid4, comment="ID")
    username = Column(
        String(length=100), nullable=False, unique=True, comment="ユーザーネーム"
    )
    digest = Column(String(length=100), nullable=False, comment="password")
    refresh_token = Column(Text, nullable=True, comment="refresh_token")
    created_at = Column(
        DateTime, nullable=False, server_default=func.now(), comment="データ登録日"
    )
    updated_at = Column(
        DateTime, nullable=True, server_onupdate=func.now(), comment="データ更新日"
    )
    deleted_at = Column(DateTime, nullable=True, comment="論理削除されたかどうか")
    participated_events = relationship(
        "Event",
        secondary=Participant.__tablename__,
        back_populates="users",
    )
    events = relationship("Event")
