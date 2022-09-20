from uuid import uuid4
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy_utils import UUIDType
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from utils.db import Base


class Category(Base):
    __tablename__ = "categories"
    __table_args__ = {"comment": "イベントカテゴリ"}

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid4, comment="ID")
    name = Column(String(length=100), nullable=False, comment="カテゴリ名")
    created_at = Column(
        DateTime, nullable=False, server_default=func.now(), comment="データ登録日"
    )
    updated_at = Column(
        DateTime, nullable=True, server_onupdate=func.now(), comment="データ更新日"
    )
    deleted_at = Column(DateTime, nullable=True, comment="論理削除されたかどうか")
    event = relationship("Event")
