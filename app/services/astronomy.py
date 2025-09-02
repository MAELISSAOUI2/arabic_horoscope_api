"""
astronomy-engine powered snapshot utilities.
"""
from datetime import datetime
from typing import Dict

from astronomy import Astronomy, Body, EclipticLongitude

from utils.arabic_nlp import AR_SIGNS
import math


def longitude_to_sign(lon_deg: float) -> str:
    idx = int(math.floor((lon_deg % 360) / 30.0)) % 12
    return AR_SIGNS[idx]


def compute_snapshot(dt: datetime) -> Dict:
    t = Astronomy.MakeTime(dt)

    bodies = {
        "sun": Body.Sun,
        "moon": Body.Moon,
        "mercury": Body.Mercury,
        "venus": Body.Venus,
        "mars": Body.Mars,
        "jupiter": Body.Jupiter,
        "saturn": Body.Saturn,
    }

    ecliptic = {}
    signs = {}
    for key, b in bodies.items():
        elon = EclipticLongitude(b, t)
        ecliptic[key] = float(elon)
        signs[key] = longitude_to_sign(float(elon))

    return {
        "utc": dt.isoformat(),
        "ecliptic_longitudes": ecliptic,
        "signs": signs,
    }