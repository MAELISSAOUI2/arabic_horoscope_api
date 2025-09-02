from pydantic import BaseModel, Field
from datetime import date
from typing import Literal, Dict, Optional

Interest = Literal["💼 عمل", "❤️ عاطفة", "💰 مال", "🧘 صحة", "🌍 عام"]


class HoroscopeRequest(BaseModel):
    الاسم: str = Field(..., min_length=1, max_length=40)
    تاريخ_الميلاد: date
    مجالات_الاهتمام: Interest


class QuantIndicators(BaseModel):
    luck: int = Field(..., ge=0, le=100)
    energy: int = Field(..., ge=0, le=100)
    mood: int = Field(..., ge=0, le=100)
    relationships: int = Field(..., ge=0, le=100)


class FreemiumResponse(BaseModel):
    premium: bool = False
    نص_قصير: str
    رمز_تعبيري: str
    sign: str
    date: str


class PremiumResponse(BaseModel):
    premium: bool = True
    تقرير_مفصل: Dict[str, str]
    مؤشرات_كمية: QuantIndicators
    نصيحة_شخصية: str
    sign: str
    date: str


class TokenRequest(BaseModel):
    email: Optional[str] = None
    name: Optional[str] = None


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class CreateCheckoutRequest(BaseModel):
    email: str
    return_url: str