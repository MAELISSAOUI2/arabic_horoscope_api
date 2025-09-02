"""
Core Horoscope Generator (Arabic) — dynamic templates + morphology + astronomy input
"""
from datetime import datetime
from typing import Dict, Any
import random


from ..services.astronomy import compute_snapshot
from ..utils.arabic_templates import (
pick_template,
WORK_TEMPLATES, LOVE_TEMPLATES, MONEY_TEMPLATES, HEALTH_TEMPLATES, ENERGY_TEMPLATES
)
from ..utils.emoji_mapper import mood_to_emoji
from ..utils.arabic_nlp import honor_name, gender_from_name, adj


PLANET_WEIGHTS = {
"sun": 3.0, "moon": 2.5, "mercury": 1.0, "venus": 1.5, "mars": 1.5, "jupiter": 2.0, "saturn": 1.5
}


ZODIAC_POLARITIES = {
"الحمل": +1, "الثور": -1, "الجوزاء": +1, "السرطان": -1, "الأسد": +1, "العذراء": -1,
"الميزان": +1, "العقرب": -1, "القوس": +1, "الجدي": -1, "الدلو": +1, "الحوت": -1,
}




def _normalize_score(x: float) -> int:
return max(0, min(100, int(round(x))))




def _affinity(a: str, b: str) -> float:
if a == b:
return 1.2
return 1.0 if ZODIAC_POLARITIES.get(a) == ZODIAC_POLARITIES.get(b) else -1.0




def build_scores(snapshot: Dict, natal_sign: str) -> Dict[str, int]:
total = 0.0
weight_sum = 0.0
for name, lon in snapshot["ecliptic_longitudes"].items():
sign = snapshot["signs"].get(name)
w = PLANET_WEIGHTS.get(name, 1.0)
total += w * _affinity(sign, natal_sign)
}