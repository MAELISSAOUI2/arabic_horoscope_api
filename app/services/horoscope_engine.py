# app/services/horoscope_engine.py
"""
Core Horoscope Generator (Arabic) — dynamic templates + morphology + astronomy input
"""
from datetime import datetime
from typing import Dict, Any
import random

from ..services.astronomy import compute_snapshot
from ..utils.arabic_templates import (
    pick_template,
    WORK_TEMPLATES, LOVE_TEMPLATES, MONEY_TEMPLATES, 
    HEALTH_TEMPLATES, ENERGY_TEMPLATES
)
from ..utils.emoji_mapper import mood_to_emoji
from ..utils.arabic_nlp import honor_name, gender_from_name, adj
from ..schemas import QuantIndicators, FreemiumResponse, PremiumResponse

PLANET_WEIGHTS = {
    "sun": 3.0, "moon": 2.5, "mercury": 1.0, 
    "venus": 1.5, "mars": 1.5, "jupiter": 2.0, "saturn": 1.5
}

ZODIAC_POLARITIES = {
    "الحمل": +1, "الثور": -1, "الجوزاء": +1, "السرطان": -1, 
    "الأسد": +1, "العذراء": -1, "الميزان": +1, "العقرب": -1, 
    "القوس": +1, "الجدي": -1, "الدلو": +1, "الحوت": -1,
}

def _normalize_score(x: float) -> int:
    return max(0, min(100, int(round(x))))

def _affinity(a: str, b: str) -> float:
    if a == b:
        return 1.2
    return 1.0 if ZODIAC_POLARITIES.get(a) == ZODIAC_POLARITIES.get(b) else 0.5

def build_scores(snapshot: Dict, natal_sign: str) -> Dict[str, int]:
    total = 0.0
    weight_sum = 0.0
    
    for name, lon in snapshot["ecliptic_longitudes"].items():
        sign = snapshot["signs"].get(name)
        w = PLANET_WEIGHTS.get(name, 1.0)
        total += w * _affinity(sign, natal_sign)
        weight_sum += w
    
    if weight_sum > 0:
        base_score = 50 + (total / weight_sum) * 30
    else:
        base_score = 50
    
    # Generate varied scores based on base
    luck = _normalize_score(base_score + random.uniform(-15, 15))
    energy = _normalize_score(base_score + random.uniform(-10, 10))
    mood = _normalize_score(base_score + random.uniform(-12, 12))
    relationships = _normalize_score(base_score + random.uniform(-8, 8))
    
    return {
        "luck": luck,
        "energy": energy, 
        "mood": mood,
        "relationships": relationships
    }

def short_horoscope_ar(name: str, natal_sign: str, interest: str, now: datetime) -> FreemiumResponse:
    snapshot = compute_snapshot(now)
    scores = build_scores(snapshot, natal_sign)
    
    honored_name = honor_name(name)
    
    # Pick template based on interest
    template_map = {
        "💼 عمل": WORK_TEMPLATES,
        "❤️ عاطفة": LOVE_TEMPLATES, 
        "💰 مال": MONEY_TEMPLATES,
        "🧘 صحة": HEALTH_TEMPLATES,
        "🌍 عام": ENERGY_TEMPLATES
    }
    
    templates = template_map.get(interest, ENERGY_TEMPLATES)
    text = pick_template(templates, name=honored_name)
    
    emoji = mood_to_emoji(scores["mood"])
    
    return FreemiumResponse(
        premium=False,
        نص_قصير=text,
        رمز_تعبيري=emoji,
        sign=natal_sign,
        date=now.strftime("%Y-%m-%d")
    )

def detailed_horoscope_ar(name: str, natal_sign: str, interest: str, now: datetime) -> PremiumResponse:
    snapshot = compute_snapshot(now)
    scores = build_scores(snapshot, natal_sign)
    
    honored_name = honor_name(name)
    
    # Generate detailed sections
    detailed_report = {
        "العمل": pick_template(WORK_TEMPLATES, name=honored_name),
        "العاطفة": pick_template(LOVE_TEMPLATES, name=honored_name),
        "المال": pick_template(MONEY_TEMPLATES, name=honored_name),
        "الصحة": pick_template(HEALTH_TEMPLATES, name=honored_name)
    }
    
    # Personal advice based on current planetary positions
    advice_templates = [
        f"{honored_name}، النجوم تشير إلى أهمية التوازن في حياتك اليوم.",
        f"اليوم مناسب للتأمل في أهدافك، {honored_name}.",
        f"ثق بحدسك اليوم، {honored_name}، فهو دليلك الأفضل."
    ]
    
    personal_advice = random.choice(advice_templates)
    
    indicators = QuantIndicators(
        luck=scores["luck"],
        energy=scores["energy"],
        mood=scores["mood"],
        relationships=scores["relationships"]
    )
    
    return PremiumResponse(
        premium=True,
        تقرير_مفصل=detailed_report,
        مؤشرات_كمية=indicators,
        نصيحة_شخصية=personal_advice,
        sign=natal_sign,
        date=now.strftime("%Y-%m-%d")
    )