from datetime import date

AR_SIGNS = [
    "الحمل", "الثور", "الجوزاء", "السرطان", "الأسد", "العذراء",
    "الميزان", "العقرب", "القوس", "الجدي", "الدلو", "الحوت"
]


def honor_name(name: str) -> str:
    """
    Process and honor the given name.
    In a more complete implementation, this could add honorifics
    or perform more sophisticated name processing.
    """
    return name.strip()


def short_paragraph(sentences: list[str]) -> str:
    """
    Join a list of sentences into a short paragraph.
    Filters out empty sentences and strips whitespace.
    """
    return " ".join(s.strip() for s in sentences if s and s.strip())


def gender_from_name(name: str) -> str:
    """
    Attempt to determine gender from Arabic name endings.
    This is a simple heuristic and may not be 100% accurate.
    
    Args:
        name: Arabic name to analyze
        
    Returns:
        "f" for feminine, "m" for masculine
    """
    name = name.strip()
    
    # Common feminine endings in Arabic names
    feminine_endings = ("ة", "ى", "ا", "ه", "اء", "ان")
    
    if name.endswith(feminine_endings):
        return "f"
    
    # Default to masculine if no feminine indicators
    return "m"


def adj(base: str, gender: str) -> str:
    """
    Adjust Arabic adjective based on gender.
    Adds feminine marker (ة) for female gender.
    
    Args:
        base: Base form of the adjective
        gender: "f" for feminine, "m" for masculine
        
    Returns:
        Adjusted adjective
    """
    if gender == "f" and not base.endswith("ة"):
        return base + "ة"
    return base


def format_arabic_date(date_obj: date) -> str:
    """
    Format a date object into Arabic date string.
    
    Args:
        date_obj: Python date object
        
    Returns:
        Formatted Arabic date string
    """
    arabic_months = {
        1: "يناير", 2: "فبراير", 3: "مارس", 4: "أبريل",
        5: "مايو", 6: "يونيو", 7: "يوليو", 8: "أغسطس",
        9: "سبتمبر", 10: "أكتوبر", 11: "نوفمبر", 12: "ديسمبر"
    }
    
    month_name = arabic_months.get(date_obj.month, "")
    return f"{date_obj.day} {month_name} {date_obj.year}"


def clean_arabic_text(text: str) -> str:
    """
    Clean and normalize Arabic text.
    
    Args:
        text: Arabic text to clean
        
    Returns:
        Cleaned text
    """
    if not text:
        return ""
    
    # Remove extra whitespace
    text = " ".join(text.split())
    
    # Ensure proper spacing around punctuation
    text = text.replace("،", "، ").replace(".", ". ").replace("!", "! ").replace("؟", "؟ ")
    
    # Remove double spaces
    while "  " in text:
        text = text.replace("  ", " ")
    
    return text.strip()


def get_zodiac_element(sign: str) -> str:
    """
    Get the element associated with a zodiac sign.
    
    Args:
        sign: Arabic zodiac sign name
        
    Returns:
        Element name in Arabic
    """
    fire_signs = ["الحمل", "الأسد", "القوس"]
    earth_signs = ["الثور", "العذراء", "الجدي"]
    air_signs = ["الجوزاء", "الميزان", "الدلو"]
    water_signs = ["السرطان", "العقرب", "الحوت"]
    
    if sign in fire_signs:
        return "نار"
    elif sign in earth_signs:
        return "تراب"
    elif sign in air_signs:
        return "هواء"
    elif sign in water_signs:
        return "ماء"
    else:
        return "غير معروف"


def is_arabic_name(name: str) -> bool:
    """
    Check if a name contains Arabic characters.
    
    Args:
        name: Name to check
        
    Returns:
        True if name contains Arabic characters
    """
    arabic_range = range(0x0600, 0x06FF + 1)
    return any(ord(char) in arabic_range for char in name)