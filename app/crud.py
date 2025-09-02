from sqlalchemy.orm import Session
from app import models
from datetime import datetime, timedelta
import json
from typing import Optional, Dict, Any

def get_or_create_user(db: Session, email: str, name: str = None):
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        user = models.User(email=email, name=name or "")
        db.add(user)
        db.commit()
        db.refresh(user)
    return user

def mark_user_premium(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        user.is_premium = True
        db.commit()

def set_user_premium(db: Session, user_id: int, until: datetime):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        user.is_premium = True
        user.premium_until = until
        db.commit()

def log_subscription_event(db: Session, user_id: int, event_type: str, raw_payload: str):
    event = models.SubscriptionEvent(
        user_id=user_id,
        event_type=event_type,
        raw_payload=raw_payload,
    )
    db.add(event)
    db.commit()

def persist_subscription_event(db: Session, user_id: int, event: dict):
    event_obj = models.SubscriptionEvent(
        user_id=user_id,
        event_type=event.get("type", "unknown"),
        raw_payload=json.dumps(event),
    )
    db.add(event_obj)
    db.commit()

def is_user_currently_premium(db: Session, user_id: int) -> bool:
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user or not user.is_premium:
        return False
    
    # Check if premium expired
    if hasattr(user, 'premium_until') and user.premium_until:
        if user.premium_until < datetime.utcnow():
            user.is_premium = False
            db.commit()
            return False
    
    return True

# Cache functions
def cache_get(db: Session, cache_key: str, tier: str) -> Optional[Dict[str, Any]]:
    cache_entry = db.query(models.CacheEntry).filter(
        models.CacheEntry.cache_key == cache_key,
        models.CacheEntry.expires_at > datetime.utcnow()
    ).first()
    
    if cache_entry:
        return json.loads(cache_entry.data)
    return None

def cache_set(db: Session, cache_key: str, tier: str, data: Dict[str, Any]):
    from app.config import settings
    
    expires_at = datetime.utcnow() + timedelta(seconds=settings.CACHE_TTL_SECONDS)
    
    cache_entry = models.CacheEntry(
        cache_key=cache_key,
        data=json.dumps(data, ensure_ascii=False),
        expires_at=expires_at
    )
    db.add(cache_entry)
    db.commit()

def log_request(db: Session, name: str, birth_date, interests: str, tier: str):
    request_log = models.RequestLog(
        name=name,
        birth_date=birth_date,
        interests=interests,
        tier=tier
    )
    db.add(request_log)
    db.commit()