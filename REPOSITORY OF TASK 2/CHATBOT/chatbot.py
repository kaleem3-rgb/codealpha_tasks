# chatbot.py

import random
from utils import detect_mood


# --- Predefined Replies (Unique & Expanded) ---

greetings = ["hi", "hello", "hey", "hola", "namaste"]
greet_replies = [
    "Hi there! 😊",
    "Hello! How can I assist you today?",
    "Hey! Good to see you!",
]

how_are_you_replies = [
    "I'm doing great! Thanks for asking 😄",
    "Functioning at 100% efficiency!",
    "I'm good. How about you?",
]

jokes = [
    "Why did the computer show up at work late? It had a hard drive 😂",
    "I'm reading a book on anti-gravity. It's impossible to put down!",
]

fallback = [
    "I'm not sure I understand 🤔",
    "Could you rephrase that?",
    "Interesting... tell me more!",
]


# --- Main Response Function ---

def get_response(user_msg):
    # Greeting check
    if user_msg in greetings:
        return random.choice(greet_replies)

    # Small talk: "how are you"
    if "how are you" in user_msg:
        return random.choice(how_are_you_replies)

    # Time request
    if "time" in user_msg:
        from datetime import datetime
        return "The current time is: " + datetime.now().strftime("%I:%M %p")

    # Joke request
    if "joke" in user_msg:
        return random.choice(jokes)

    # Mood detection (smart + unique)
    mood = detect_mood(user_msg)
    if mood == "positive":
        return "I'm glad you're feeling good! 😊"
    elif mood == "negative":
        return "I'm sorry you're feeling like that. I'm here to chat. ❤️"

    # Default fallback
    return random.choice(fallback)
