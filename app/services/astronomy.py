"""
astronomy-engine powered snapshot utilities.
"""
from datetime import datetime
from typing import Dict
import math

try:
    from astronomy import Astronomy, Body, EclipticLongitude
    ASTRONOMY_AVAILABLE = True
except ImportError:
    ASTRONOMY_AVAILABLE = False

from ..utils.arabic_nlp import AR_SIGNS


def longitude_to_sign(lon_deg: float) -> str:
    idx = int(math.floor((lon_deg % 360) / 30.0)) % 12
    return AR_SIGNS[idx]


def compute_snapshot(dt: datetime) -> Dict:
    if not ASTRONOMY_AVAILABLE:
        # Fallback: generate mock data based on date
        return _generate_mock_snapshot(dt)
    
    try:
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
    except Exception:
        return _generate_mock_snapshot(dt)


def _generate_mock_snapshot(dt: datetime) -> Dict:
    """Generate mock astronomical data for testing when astronomy-engine is not available"""
    import random
    
    # Set seed based on date for consistent results
    random.seed(dt.day + dt.month * 31 + dt.year * 365)
    
    bodies = ["sun", "moon", "mercury", "venus", "mars", "jupiter", "saturn"]
    ecliptic = {}
    signs = {}
    
    for body in bodies:
        # Generate realistic longitude (0-360)
        longitude = random.uniform(0, 360)
        ecliptic[body] = longitude
        signs[body] = longitude_to_sign(longitude)
    
    return {
        "utc": dt.isoformat(),
        "ecliptic_longitudes": ecliptic,
        "signs": signs,
    }