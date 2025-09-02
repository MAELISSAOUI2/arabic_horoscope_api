from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import hashlib
from sqlalchemy.orm import Session

# Fixed relative imports
from .config import settings
from .database import Base, engine, get_db
from .schemas import (
    HoroscopeRequest, FreemiumResponse, PremiumResponse,
    TokenRequest, TokenResponse, CreateCheckoutRequest
)
from .services.tiers import resolve_tier
from .services.horoscope_engine import short_horoscope_ar, detailed_horoscope_ar
from .services.astronomy import compute_snapshot
from .services.auth import create_access_token, decode_token
from .services.billing import create_konnect_checkout, handle_konnect_event
from .utils.arabic_nlp import AR_SIGNS
from . import crud

# Initialize FastAPI app
app = FastAPI(title=settings.APP_NAME, version=settings.VERSION)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[o.strip() for o in settings.ALLOW_ORIGINS.split(",")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Create database tables
Base.metadata.create_all(bind=engine)


def _sign_by_birthdate(birth_date) -> str:
    """
    Determine zodiac sign based on birth date using fixed date ranges.
    Uses Western tropical zodiac system.
    """
    mmdd = int(birth_date.strftime("%m%d"))
    
    # Date ranges for zodiac signs (month-day format)
    ranges = [
        (321, 419, "الحمل"),      # Aries: March 21 - April 19
        (420, 520, "الثور"),      # Taurus: April 20 - May 20
        (521, 620, "الجوزاء"),    # Gemini: May 21 - June 20
        (621, 722, "السرطان"),    # Cancer: June 21 - July 22
        (723, 822, "الأسد"),      # Leo: July 23 - August 22
        (823, 922, "العذراء"),    # Virgo: August 23 - September 22
        (923, 1022, "الميزان"),   # Libra: September 23 - October 22
        (1023, 1121, "العقرب"),   # Scorpio: October 23 - November 21
        (1122, 1221, "القوس"),    # Sagittarius: November 22 - December 21
        (1222, 119, "الجدي"),     # Capricorn: December 22 - January 19
        (120, 218, "الدلو"),      # Aquarius: January 20 - February 18
        (219, 320, "الحوت")       # Pisces: February 19 - March 20
    ]
    
    for start, end, name in ranges:
        if start <= end:
            # Normal range within same year
            if start <= mmdd <= end:
                return name
        else:
            # Range wraps around year end (like Capricorn)
            if mmdd >= start or mmdd <= end:
                return name
    
    # Default fallback
    return "الحمل"


@app.post("/horoscope", response_model=FreemiumResponse | PremiumResponse)
async def get_horoscope(
    body: HoroscopeRequest,
    tier: str = Depends(resolve_tier),
    db: Session = Depends(get_db)
):
    """
    Generate horoscope based on user input and tier level.
    Returns either freemium (basic) or premium (detailed) response.
    """
    try:
        # Create cache key for request deduplication
        today = datetime.utcnow().date().isoformat()
        cache_key_raw = (
            f"{body.الاسم}|{body.تاريخ_الميلاد.isoformat()}|"
            f"{body.مجالات_الاهتمام}|{today}|{tier}"
        )
        cache_key = hashlib.sha256(cache_key_raw.encode("utf-8")).hexdigest()

        # Check cache first
        cached = crud.cache_get(db, cache_key, tier)
        if cached:
            return cached

        # Determine zodiac sign from birth date
        natal_sign = _sign_by_birthdate(body.تاريخ_الميلاد)

        # Generate horoscope based on tier
        now = datetime.utcnow()
        if tier == "freemium":
            payload = short_horoscope_ar(
                body.الاسم, natal_sign, body.مجالات_الاهتمام, now
            )
        else:
            payload = detailed_horoscope_ar(
                body.الاسم, natal_sign, body.مجالات_الاهتمام, now
            )

        # Cache the result
        crud.cache_set(db, cache_key, tier, payload.dict())
        
        # Log the request for analytics
        crud.log_request(
            db, body.الاسم, body.تاريخ_الميلاد, body.مجالات_الاهتمام, tier
        )
        
        return payload

    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Error generating horoscope: {str(e)}"
        )


@app.post("/auth/token", response_model=TokenResponse)
async def login(body: TokenRequest, db: Session = Depends(get_db)):
    """
    Generate JWT token for user authentication.
    Creates user if doesn't exist.
    """
    try:
        if not body.email:
            raise HTTPException(status_code=400, detail="Email is required")
        
        token = create_access_token(db, body.email, body.name)
        return TokenResponse(access_token=token)
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Authentication error: {str(e)}")


@app.post("/billing/checkout")
async def create_checkout(body: CreateCheckoutRequest):
    """
    Create Konnect payment checkout session.
    Returns checkout URL for premium subscription.
    """
    try:
        if not body.email:
            raise HTTPException(status_code=400, detail="Email is required")
        if not body.return_url:
            raise HTTPException(status_code=400, detail="Return URL is required")
        
        result = await create_konnect_checkout(body.email, body.return_url)
        return result
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Checkout error: {str(e)}")


@app.post("/billing/webhook")
async def billing_webhook(request: Request, db: Session = Depends(get_db)):
    """
    Handle Konnect payment webhook events.
    Updates user premium status based on payment events.
    """
    try:
        # Get raw body as JSON
        event = await request.json()
        
        # Process the webhook event
        await handle_konnect_event(db, event)
        
        return {"status": "success", "message": "Webhook processed"}
    
    except Exception as e:
        # Log error but return 200 to prevent webhook retries
        print(f"Webhook error: {str(e)}")
        return {"status": "error", "message": str(e)}


@app.get("/health")
async def health():
    """
    Health check endpoint.
    Verifies API status and astronomical calculation availability.
    """
    status = "ok"
    details = {}
    
    try:
        # Test astronomical calculations
        snapshot = compute_snapshot(datetime.utcnow())
        details["astronomy"] = "available"
        details["planets_checked"] = len(snapshot.get("ecliptic_longitudes", {}))
    except Exception as e:
        status = "degraded"
        details["astronomy"] = f"error: {str(e)}"
    
    try:
        # Test database connection
        from .database import SessionLocal
        db = SessionLocal()
        db.execute("SELECT 1")
        db.close()
        details["database"] = "connected"
    except Exception as e:
        status = "degraded"
        details["database"] = f"error: {str(e)}"
    
    return {
        "status": status,
        "version": settings.VERSION,
        "details": details,
        "timestamp": datetime.utcnow().isoformat()
    }


@app.get("/")
async def root():
    """
    Root endpoint with API information.
    """
    return {
        "name": settings.APP_NAME,
        "version": settings.VERSION,
        "description": "Arabic Daily Horoscope API with premium features",
        "endpoints": {
            "horoscope": "POST /horoscope - Generate horoscope",
            "auth": "POST /auth/token - Get authentication token",
            "billing": "POST /billing/checkout - Create payment session",
            "health": "GET /health - Health check"
        }
    }


@app.get("/signs")
async def get_zodiac_signs():
    """
    Get all zodiac signs in Arabic with their date ranges.
    Useful for frontend integration.
    """
    from .constants import ZODIAC_SIGNS
    
    return {
        "signs": {
            sign_key: {
                "arabic_name": data["arabic_name"],
                "english_name": data["english_name"],
                "dates": {
                    "start": f"{data['dates'][0][0]}-{data['dates'][0][1]:02d}",
                    "end": f"{data['dates'][1][0]}-{data['dates'][1][1]:02d}"
                },
                "element": data["element"],
                "symbol": data["symbol"]
            }
            for sign_key, data in ZODIAC_SIGNS.items()
        }
    }


# Error handlers
@app.exception_handler(404)
async def not_found_handler(request: Request, exc):
    return {
        "error": "Not Found",
        "message": "The requested endpoint does not exist",
        "path": str(request.url.path)
    }


@app.exception_handler(500)
async def internal_error_handler(request: Request, exc):
    return {
        "error": "Internal Server Error",
        "message": "An unexpected error occurred",
        "path": str(request.url.path)
    }


# Startup event
@app.on_event("startup")
async def startup_event():
    """
    Application startup tasks.
    """
    print(f"Starting {settings.APP_NAME} v{settings.VERSION}")
    print(f"Environment: {settings.ENV}")
    
    # Test critical dependencies
    try:
        compute_snapshot(datetime.utcnow())
        print("✓ Astronomical calculations working")
    except Exception as e:
        print(f"✗ Astronomical calculations failed: {e}")
    
    try:
        from .database import SessionLocal
        db = SessionLocal()
        db.execute("SELECT 1")
        db.close()
        print("✓ Database connection working")
    except Exception as e:
        print(f"✗ Database connection failed: {e}")


# Shutdown event
@app.on_event("shutdown")
async def shutdown_event():
    """
    Application shutdown tasks.
    """
    print(f"Shutting down {settings.APP_NAME}")