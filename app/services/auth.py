import jwt
from datetime import datetime, timedelta
from fastapi import HTTPException, Header
from typing import Optional
from ..config import settings
from ..crud import get_or_create_user




def create_access_token(db, user_email: str, user_name: str = None):
user = get_or_create_user(db, email=user_email, name=user_name)
expire = datetime.utcnow() + timedelta(days=settings.JWT_EXPIRE_DAYS)
payload = {
"sub": str(user.id),
"email": user_email,
"exp": int(expire.timestamp()),
"is_premium": user.is_premium,
}
token = jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
return token




def decode_token(token: str):
try:
data = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
return data
except jwt.ExpiredSignatureError:
raise HTTPException(status_code=401, detail="token_expired")
except Exception:
raise HTTPException(status_code=401, detail="invalid_token")