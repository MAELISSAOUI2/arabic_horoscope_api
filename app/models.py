from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    is_premium = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    subscriptions = relationship(
        "SubscriptionEvent",
        back_populates="user",
        cascade="all, delete-orphan"
    )


class SubscriptionEvent(Base):
    __tablename__ = "subscription_events"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    event_type = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    raw_payload = Column(String)

    user = relationship("User", back_populates="subscriptions")