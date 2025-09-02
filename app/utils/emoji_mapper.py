def mood_to_emoji(score: int) -> str:
if score >= 80:
return "🌞"
if score >= 60:
return "✨"
if score >= 40:
return "🌙"
if score >= 20:
return "⛅"
return "🌫️"