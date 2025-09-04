def mood_to_emoji(score: int) -> str:
    """
    Map a mood score to an appropriate emoji.
    
    Args:
        score: Mood score from 0-100
        
    Returns:
        Emoji string representing the mood
    """
    if score >= 80:
        return "🌞"
    if score >= 60:
        return "✨"
    if score >= 40:
        return "🌙"
    if score >= 20:
        return "⛅"
    return "🌫️"