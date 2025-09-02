from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import hashlib

from .config import settings
from database import Base, engine, get_db
from schemas import HoroscopeRequest, FreemiumResponse, PremiumResponse
from services.tiers import resolve_tier
from services.horoscope_engine import short_horoscope_ar, detailed_horoscope_ar
from services.astronomy import compute_snapshot
from utils.arabic_nlp import AR_SIGNS
from crud import cache_get, cache_set, log_request

from sqlalchemy.orm import Session

app = FastAPI(title=settings.APP_NAME, version=settings.VERSION)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[o.strip() for o in settings.ALLOW_ORIGINS.split(",")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Create tables
Base.metadata.create_all(bind=engine)


def _sign_by_birthdate(birth_date) -> str:
    # Approximate: map by solar ecliptic longitude based on Western tropical zodiac.
    # Simpler: fixed date ranges (good first cut; can be refined later to exact solstice-based logic).
    # Dates are inclusive of start.
    mmdd = int(birth_date.strftime("%m%d"))
    ranges = [
        (321, 419, "الحمل"), (420, 520, "الثور"), (521, 620, "الجوزاء"),
        (621, 722, "السرطان"), (723, 822, "الأسد"), (823, 922, "العذراء"),
        (923, 1022, "الميزان"), (1023, 1121, "العقرب"), (1122, 1221, "القوس"),
        (1222, 119, "الجدي"), (120, 218, "الدلو"), (219, 320, "الحوت")
    ]
    for start, end, name in ranges:
        if start <= end:
            if start <= mmdd <= end:
                return name
        else:  # wraps year end
            if mmdd >= start or mmdd <= end:
                return name
    return "الحمل"


@app.post("/horoscope", response_model=FreemiumResponse | PremiumResponse)
async def get_horoscope(
    body: HoroscopeRequest,
    tier: str = Depends(resolve_tier),
    db: Session = Depends(get_db)
):
    # Rate-limit: freemium → 1 per day per name+birthdate
    today = datetime.utcnow().date().isoformat()
    cache_key_raw = (
        f"{body.الاسم}|{body.تاريخ_الميلاد.isoformat()}|"
        f"{body.مجالات_الاهتمام}|{today}|{tier}"
    )
    cache_key = hashlib.sha256(cache_key_raw.encode("utf-8")).hexdigest()

    cached = cache_get(db, cache_key, tier)
    if cached:
        return cached

    natal_sign = _sign_by_birthdate(body.تاريخ_الميلاد)

    now = datetime.utcnow()
    if tier == "freemium":
        payload = short_horoscope_ar(
            body.الاسم, natal_sign, body.مجالات_الاهتمام, now
        )
    else:
        payload = detailed_horoscope_ar(
            body.الاسم, natal_sign, body.مجالات_الاهتمام, now
        )

    cache_set(db, cache_key, tier, payload)
    log_request(
        db, body.الاسم, body.تاريخ_الميلاد, body.مجالات_الاهتمام, tier
    )
    return payload


@app.get("/health")
async def health():
    # also verifies ephemeris available
    status = "ok"
    try:
        compute_snapshot(datetime.utcnow())
    except Exception as e:
        status = f"degraded: {e}"
    return {"status": status, "version": settings.VERSION}