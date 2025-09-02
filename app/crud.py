from sqlalchemy.orm import Session
from app import models


def get_or_create_user(db: Session, email: str):
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        user = models.User(email=email)
        db.add(user)
        db.commit()
        db.refresh(user)
    return user


def mark_user_premium(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        user.is_premium = True
        db.commit()


def log_subscription_event(db: Session, user_id: int, event_type: str, raw_payload: str):
    event = models.SubscriptionEvent(
        user_id=user_id,
        event_type=event_type,
        raw_payload=raw_payload,
    )
    db.add(event)
    db.commit()


def is_user_currently_premium(db: Session, user_id: int) -> bool:
    user = db.query(models.User).filter(models.User.id == user_id).first()
    return bool(user and user.is_premium)