from datetime import date


AR_SIGNS = [
"الحمل", "الثور", "الجوزاء", "السرطان", "الأسد", "العذراء",
"الميزان", "العقرب", "القوس", "الجدي", "الدلو", "الحوت"
]




def honor_name(name: str) -> str:
return name.strip()




def short_paragraph(sentences: list[str]) -> str:
return " ".join(s.strip() for s in sentences if s and s.strip())




def gender_from_name(name: str) -> str:
name = name.strip()
if name.endswith(("ة", "ى", "ا", "ه")):
return "f"
return "m"




def adj(base: str, gender: str) -> str:
if gender == "f":
return base + "ة"
return base