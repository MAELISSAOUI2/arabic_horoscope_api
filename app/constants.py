# constants.py
# Enhanced constants for Arabic horoscope API with comprehensive astrological data

# ZODIAC_SIGNS constant with enhanced data
ZODIAC_SIGNS = {
    "aries": {
        "dates": ((3, 21), (4, 19)),
        "arabic_name": "الحمل",
        "english_name": "Aries",
        "element": "نار",
        "quality": "كاردينال",
        "ruling_planet": "المريخ",
        "symbol": "♈",
        "keywords": ["قيادة", "شجاعة", "مبادرة", "طاقة"],
        "colors": ["الأحمر", "البرتقالي"],
        "lucky_numbers": [1, 8, 17],
        "body_parts": ["الرأس", "الوجه"],
        "stones": ["الياقوت", "العقيق الأحمر"]
    },
    "taurus": {
        "dates": ((4, 20), (5, 20)),
        "arabic_name": "الثور",
        "english_name": "Taurus",
        "element": "تراب",
        "quality": "ثابت",
        "ruling_planet": "الزهرة",
        "symbol": "♉",
        "keywords": ["استقرار", "صبر", "عملية", "جمال"],
        "colors": ["الأخضر", "الوردي"],
        "lucky_numbers": [2, 6, 9],
        "body_parts": ["العنق", "الحلق"],
        "stones": ["الزمرد", "الكوارتز الوردي"]
    },
    "gemini": {
        "dates": ((5, 21), (6, 20)),
        "arabic_name": "الجوزاء",
        "english_name": "Gemini",
        "element": "هواء",
        "quality": "متحرك",
        "ruling_planet": "عطارد",
        "symbol": "♊",
        "keywords": ["تواصل", "ذكاء", "مرونة", "فضول"],
        "colors": ["الأصفر", "الفضي"],
        "lucky_numbers": [5, 7, 14],
        "body_parts": ["الذراعين", "الرئتين"],
        "stones": ["العقيق", "السيترين"]
    },
    "cancer": {
        "dates": ((6, 21), (7, 22)),
        "arabic_name": "السرطان",
        "english_name": "Cancer",
        "element": "ماء",
        "quality": "كاردينال",
        "ruling_planet": "القمر",
        "symbol": "♋",
        "keywords": ["عاطفة", "حدس", "أمومة", "حماية"],
        "colors": ["الفضي", "الأبيض"],
        "lucky_numbers": [2, 7, 11],
        "body_parts": ["الصدر", "المعدة"],
        "stones": ["اللؤلؤ", "حجر القمر"]
    },
    "leo": {
        "dates": ((7, 23), (8, 22)),
        "arabic_name": "الأسد",
        "english_name": "Leo",
        "element": "نار",
        "quality": "ثابت",
        "ruling_planet": "الشمس",
        "symbol": "♌",
        "keywords": ["كرامة", "إبداع", "كبرياء", "كرم"],
        "colors": ["الذهبي", "البرتقالي"],
        "lucky_numbers": [1, 3, 10],
        "body_parts": ["القلب", "الظهر"],
        "stones": ["الياقوت الأصفر", "العنبر"]
    },
    "virgo": {
        "dates": ((8, 23), (9, 22)),
        "arabic_name": "العذراء",
        "english_name": "Virgo",
        "element": "تراب",
        "quality": "متحرك",
        "ruling_planet": "عطارد",
        "symbol": "♍",
        "keywords": ["تحليل", "خدمة", "كمال", "صحة"],
        "colors": ["البني", "الأخضر الداكن"],
        "lucky_numbers": [6, 15, 20],
        "body_parts": ["الأمعاء", "الجهاز الهضمي"],
        "stones": ["الياقوت الأزرق", "العقيق الأخضر"]
    },
    "libra": {
        "dates": ((9, 23), (10, 22)),
        "arabic_name": "الميزان",
        "english_name": "Libra",
        "element": "هواء",
        "quality": "كاردينال",
        "ruling_planet": "الزهرة",
        "symbol": "♎",
        "keywords": ["عدالة", "توازن", "انسجام", "دبلوماسية"],
        "colors": ["الوردي", "الأزرق الفاتح"],
        "lucky_numbers": [6, 15, 24],
        "body_parts": ["الكلى", "أسفل الظهر"],
        "stones": ["الأوبال", "اللازورد"]
    },
    "scorpio": {
        "dates": ((10, 23), (11, 21)),
        "arabic_name": "العقرب",
        "english_name": "Scorpio",
        "element": "ماء",
        "quality": "ثابت",
        "ruling_planet": "المريخ",
        "symbol": "♏",
        "keywords": ["تحول", "قوة", "غموض", "عمق"],
        "colors": ["الأحمر الداكن", "الأسود"],
        "lucky_numbers": [8, 13, 27],
        "body_parts": ["الأعضاء التناسلية", "المثانة"],
        "stones": ["التوباز", "العقيق الأحمر الداكن"]
    },
    "sagittarius": {
        "dates": ((11, 22), (12, 21)),
        "arabic_name": "القوس",
        "english_name": "Sagittarius",
        "element": "نار",
        "quality": "متحرك",
        "ruling_planet": "المشتري",
        "symbol": "♐",
        "keywords": ["حكمة", "سفر", "فلسفة", "مغامرة"],
        "colors": ["البنفسجي", "التركواز"],
        "lucky_numbers": [9, 18, 27],
        "body_parts": ["الفخذين", "الوركين"],
        "stones": ["الفيروز", "الجمشت"]
    },
    "capricorn": {
        "dates": ((12, 22), (1, 19)),
        "arabic_name": "الجدي",
        "english_name": "Capricorn",
        "element": "تراب",
        "quality": "كاردينال",
        "ruling_planet": "زحل",
        "symbol": "♑",
        "keywords": ["انضباط", "مسؤولية", "طموح", "تقليد"],
        "colors": ["الأسود", "البني الداكن"],
        "lucky_numbers": [10, 22, 26],
        "body_parts": ["الركبتين", "العظام"],
        "stones": ["الجارنت", "الأونكس"]
    },
    "aquarius": {
        "dates": ((1, 20), (2, 18)),
        "arabic_name": "الدلو",
        "english_name": "Aquarius",
        "element": "هواء",
        "quality": "ثابت",
        "ruling_planet": "زحل",
        "symbol": "♒",
        "keywords": ["إنسانية", "ابتكار", "استقلالية", "مستقبل"],
        "colors": ["الأزرق الكهربائي", "الفضي"],
        "lucky_numbers": [4, 7, 11],
        "body_parts": ["الساقين", "الكاحلين"],
        "stones": ["الأكوامارين", "الجمشت"]
    },
    "pisces": {
        "dates": ((2, 19), (3, 20)),
        "arabic_name": "الحوت",
        "english_name": "Pisces",
        "element": "ماء",
        "quality": "متحرك",
        "ruling_planet": "المشتري",
        "symbol": "♓",
        "keywords": ["حدس", "خيال", "روحانية", "تعاطف"],
        "colors": ["الأخضر البحري", "اللافندر"],
        "lucky_numbers": [3, 9, 12],
        "body_parts": ["القدمين", "الجهاز اللمفاوي"],
        "stones": ["الأكوامارين", "الأماثيست"]
    }
}

# PLANETS_ARABIC constant with enhanced planetary information
PLANETS_ARABIC = {
    "sun": {
        "arabic": "الشمس",
        "symbol": "☉",
        "element": "نار",
        "day": "الأحد",
        "metal": "الذهب",
        "color": "الذهبي",
        "keywords": ["الذات", "الهوية", "الحيوية", "القيادة"]
    },
    "moon": {
        "arabic": "القمر",
        "symbol": "☽",
        "element": "ماء",
        "day": "الاثنين",
        "metal": "الفضة",
        "color": "الفضي",
        "keywords": ["العواطف", "الحدس", "الذاكرة", "الأمومة"]
    },
    "mercury": {
        "arabic": "عطارد",
        "symbol": "☿",
        "element": "هواء",
        "day": "الأربعاء",
        "metal": "الزئبق",
        "color": "الأصفر",
        "keywords": ["التواصل", "الذكاء", "التجارة", "السفر"]
    },
    "venus": {
        "arabic": "الزهرة",
        "symbol": "♀",
        "element": "تراب",
        "day": "الجمعة",
        "metal": "النحاس",
        "color": "الوردي",
        "keywords": ["الحب", "الجمال", "الفن", "الانسجام"]
    },
    "mars": {
        "arabic": "المريخ",
        "symbol": "♂",
        "element": "نار",
        "day": "الثلاثاء",
        "metal": "الحديد",
        "color": "الأحمر",
        "keywords": ["الطاقة", "الشجاعة", "الحرب", "الشغف"]
    },
    "jupiter": {
        "arabic": "المشتري",
        "symbol": "♃",
        "element": "نار",
        "day": "الخميس",
        "metal": "القصدير",
        "color": "البنفسجي",
        "keywords": ["الحكمة", "التوسع", "الحظ", "الفلسفة"]
    },
    "saturn": {
        "arabic": "زحل",
        "symbol": "♄",
        "element": "تراب",
        "day": "السبت",
        "metal": "الرصاص",
        "color": "الأسود",
        "keywords": ["الانضباط", "الحدود", "الدروس", "الوقت"]
    },
    "uranus": {
        "arabic": "أورانوس",
        "symbol": "♅",
        "element": "هواء",
        "day": "الأربعاء",
        "metal": "اليورانيوم",
        "color": "الأزرق الكهربائي",
        "keywords": ["التغيير", "الثورة", "الابتكار", "الحرية"]
    },
    "neptune": {
        "arabic": "نبتون",
        "symbol": "♆",
        "element": "ماء",
        "day": "الخميس",
        "metal": "البلاتين",
        "color": "الأخضر البحري",
        "keywords": ["الأحلام", "الوهم", "الروحانية", "الخيال"]
    },
    "pluto": {
        "arabic": "بلوتو",
        "symbol": "♇",
        "element": "ماء",
        "day": "الثلاثاء",
        "metal": "البلوتونيوم",
        "color": "الأحمر الداكن",
        "keywords": ["التحول", "القوة", "الموت والولادة", "اللاوعي"]
    }
}

# HOUSES_ARABIC - Astrological houses in Arabic tradition
HOUSES_ARABIC = {
    1: {
        "arabic": "البيت الأول",
        "english": "First House",
        "meaning": "الشخصية والمظهر",
        "keywords": ["الذات", "المظهر", "الهوية", "البداية"],
        "body_parts": ["الرأس", "الوجه"]
    },
    2: {
        "arabic": "البيت الثاني",
        "english": "Second House",
        "meaning": "المال والممتلكات",
        "keywords": ["المال", "القيم", "الممتلكات", "الموارد"],
        "body_parts": ["العنق", "الحلق"]
    },
    3: {
        "arabic": "البيت الثالث",
        "english": "Third House",
        "meaning": "التواصل والأشقاء",
        "keywords": ["التواصل", "الأشقاء", "السفر القصير", "التعلم"],
        "body_parts": ["الذراعين", "اليدين"]
    },
    4: {
        "arabic": "البيت الرابع",
        "english": "Fourth House",
        "meaning": "البيت والعائلة",
        "keywords": ["البيت", "العائلة", "الجذور", "الأم"],
        "body_parts": ["الصدر", "المعدة"]
    },
    5: {
        "arabic": "البيت الخامس",
        "english": "Fifth House",
        "meaning": "الحب والأطفال",
        "keywords": ["الحب", "الأطفال", "الإبداع", "المتعة"],
        "body_parts": ["القلب", "الظهر"]
    },
    6: {
        "arabic": "البيت السادس",
        "english": "Sixth House",
        "meaning": "الصحة والعمل",
        "keywords": ["الصحة", "العمل", "الخدمة", "الروتين"],
        "body_parts": ["الأمعاء", "الجهاز الهضمي"]
    },
    7: {
        "arabic": "البيت السابع",
        "english": "Seventh House",
        "meaning": "الشراكة والزواج",
        "keywords": ["الزواج", "الشراكة", "العلاقات", "الأعداء المكشوفين"],
        "body_parts": ["الكلى", "أسفل الظهر"]
    },
    8: {
        "arabic": "البيت الثامن",
        "english": "Eighth House",
        "meaning": "التحول والموت",
        "keywords": ["التحول", "الموت", "الولادة", "الأسرار"],
        "body_parts": ["الأعضاء التناسلية"]
    },
    9: {
        "arabic": "البيت التاسع",
        "english": "Ninth House",
        "meaning": "الفلسفة والسفر",
        "keywords": ["الفلسفة", "السفر الطويل", "التعليم العالي", "الدين"],
        "body_parts": ["الفخذين", "الوركين"]
    },
    10: {
        "arabic": "البيت العاشر",
        "english": "Tenth House",
        "meaning": "المهنة والسمعة",
        "keywords": ["المهنة", "السمعة", "المكانة", "الأب"],
        "body_parts": ["الركبتين", "العظام"]
    },
    11: {
        "arabic": "البيت الحادي عشر",
        "english": "Eleventh House",
        "meaning": "الأصدقاء والأماني",
        "keywords": ["الأصدقاء", "الأماني", "المجموعات", "الآمال"],
        "body_parts": ["الساقين", "الكاحلين"]
    },
    12: {
        "arabic": "البيت الثاني عشر",
        "english": "Twelfth House",
        "meaning": "الأسرار واللاوعي",
        "keywords": ["الأسرار", "اللاوعي", "الكرما", "الأعداء الخفيين"],
        "body_parts": ["القدمين"]
    }
}

# ASPECTS_ARABIC - Astrological aspects in Arabic
ASPECTS_ARABIC = {
    "conjunction": {
        "arabic": "اقتران",
        "symbol": "☌",
        "angle": 0,
        "orb": 8,
        "nature": "محايد",
        "description": "اتحاد الطاقات"
    },
    "sextile": {
        "arabic": "تسديس",
        "symbol": "⚹",
        "angle": 60,
        "orb": 6,
        "nature": "مفيد",
        "description": "تناغم وفرص"
    },
    "square": {
        "arabic": "تربيع",
        "symbol": "□",
        "angle": 90,
        "orb": 8,
        "nature": "صعب",
        "description": "توتر وتحدي"
    },
    "trine": {
        "arabic": "تثليث",
        "symbol": "△",
        "angle": 120,
        "orb": 8,
        "nature": "مفيد",
        "description": "انسجام طبيعي"
    },
    "opposition": {
        "arabic": "مقابلة",
        "symbol": "☍",
        "angle": 180,
        "orb": 8,
        "nature": "متوتر",
        "description": "صراع وتوازن"
    }
}

# ARABIC_MONTHS - Arabic month names
ARABIC_MONTHS = {
    1: "يناير", 2: "فبراير", 3: "مارس", 4: "أبريل",
    5: "مايو", 6: "يونيو", 7: "يوليو", 8: "أغسطس",
    9: "سبتمبر", 10: "أكتوبر", 11: "نوفمبر", 12: "ديسمبر"
}

# ARABIC_DAYS - Arabic day names
ARABIC_DAYS = {
    0: "الاثنين", 1: "الثلاثاء", 2: "الأربعاء", 3: "الخميس",
    4: "الجمعة", 5: "السبت", 6: "الأحد"
}

# ELEMENTS_ARABIC - Enhanced element information
ELEMENTS_ARABIC = {
    "نار": {
        "english": "Fire",
        "qualities": ["حيوية", "نشاط", "إبداع", "قيادة"],
        "colors": ["الأحمر", "البرتقالي", "الذهبي"],
        "season": "الصيف",
        "direction": "الجنوب"
    },
    "تراب": {
        "english": "Earth", 
        "qualities": ["استقرار", "عملية", "موثوقية", "صبر"],
        "colors": ["الأخضر", "البني", "الأصفر"],
        "season": "الخريف",
        "direction": "الشمال"
    },
    "هواء": {
        "english": "Air",
        "qualities": ["ذكاء", "تواصل", "مرونة", "اجتماعية"],
        "colors": ["الأصفر", "الفضي", "الأبيض"],
        "season": "الربيع",
        "direction": "الشرق"
    },
    "ماء": {
        "english": "Water",
        "qualities": ["عاطفة", "حدس", "تعاطف", "إبداع"],
        "colors": ["الأزرق", "الفضي", "البنفسجي"],
        "season": "الشتاء",
        "direction": "الغرب"
    }
}

# API_MESSAGES - Standard API response messages in Arabic
API_MESSAGES = {
    "success": {
        "profile_created": "تم إنشاء الملف الشخصي بنجاح",
        "profile_updated": "تم تحديث الملف الشخصي بنجاح",
        "horoscope_generated": "تم إنتاج البرج بنجاح"
    },
    "errors": {
        "user_not_found": "المستخدم غير موجود",
        "invalid_location": "الموقع غير صحيح",
        "calculation_error": "خطأ في الحسابات الفلكية",
        "invalid_date": "التاريخ غير صحيح",
        "invalid_time": "الوقت غير صحيح",
        "geocoding_timeout": "انتهت مهلة تحديد الموقع",
        "database_error": "خطأ في قاعدة البيانات"
    },
    "warnings": {
        "using_default_time": "تم استخدام الوقت الافتراضي (12:00)",
        "cached_result": "تم إرجاع نتيجة محفوظة مسبقاً"
    }
}