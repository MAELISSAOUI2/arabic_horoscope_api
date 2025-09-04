import httpx
from fastapi import HTTPException
from ..config import settings
from datetime import datetime, timedelta


async def create_konnect_checkout(email: str, return_url: str) -> dict:
    """
    Create a checkout session in Konnect.
    This function assumes Konnect returns a JSON with a checkout_url and session_id.
    Replace the URL & payload as per Konnect API docs.
    """
    payload = {
        "product_id": settings.PREMIUM_PRODUCT_ID,
        "customer_email": email,
        "return_url": return_url
    }
    headers = {
        "Authorization": f"Bearer {settings.KONNECT_API_KEY}", 
        "Content-Type": "application/json"
    }
    
    async with httpx.AsyncClient(timeout=10) as client:
        resp = await client.post(settings.KONNECT_API_URL, json=payload, headers=headers)
        if resp.status_code != 200:
            raise HTTPException(status_code=502, detail="konnect_unavailable")
        return resp.json()


async def handle_konnect_event(db, event: dict):
    """
    Minimal handler: expects event to contain customer_email, status, and period_end.
    Persist event and mark user premium if active.
    """
    from ..crud import get_or_create_user, persist_subscription_event, set_user_premium
    
    data = event.get("data", {})
    email = data.get("customer_email")
    status = data.get("status")
    period_end = data.get("period_end")
    
    if not email:
        return
    
    user = get_or_create_user(db, email=email)
    persist_subscription_event(db, user.id, event)
    
    if status == "active" and period_end:
        until = datetime.fromisoformat(period_end.replace('Z', '+00:00'))
        set_user_premium(db, user.id, until)