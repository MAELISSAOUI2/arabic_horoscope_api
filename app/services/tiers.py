from fastapi import Header
from typing import Optional
from ..services.auth import decode_token
from ..crud import is_user_currently_premium
from ..database import SessionLocal


async def resolve_tier(authorization: Optional[str] = Header(default=None)) -> str:
"""
Determine tier from Authorization: Bearer <token>
If valid JWT and user is premium (by DB), return 'premium'. Else freemium.
"""
if not authorization:
return "freemium"
parts = authorization.split()
if len(parts) != 2 or parts[0].lower() != 'bearer':
return "freemium"
token = parts[1]
try:
data = decode_token(token)
except Exception:
return "freemium"
user_id = int(data.get('sub'))
db = SessionLocal()
try:
if is_user_currently_premium(db, user_id):
return "premium"
finally:
db.close()
return "freemium"