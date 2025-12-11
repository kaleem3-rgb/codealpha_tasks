# utils.py

# --- Mood Word Lists ---
positive_words = [
    "good", "great", "happy", "awesome", "fantastic",
    "love", "excited", "nice", "cool"
]

negative_words = [
    "sad", "bad", "upset", "angry", "tired",
    "depressed", "annoyed", "hate"
]


def detect_mood(text):
    """
    Detects simple positive/negative emotions in user messages.
    Returns: 'positive', 'negative', or 'neutral'
    """

    text = text.lower()

    # Check for positive tone
    for word in positive_words:
        if word in text:
            return "positive"

    # Check for negative tone
    for word in negative_words:
        if word in text:
            return "negative"

    return "neutral"