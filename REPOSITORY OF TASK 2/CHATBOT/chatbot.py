# chatbot.py

import random
from utils import detect_mood


# --- Predefined Replies (Unique & Expanded) ---

greetings = [
    "hi", 
    "hello",
    "hey", 
    "hola",
    "namaste"
    ]

greet_replies = [
    "Hi there! 😊",
    "Hello! How can I assist you today?",
    "Hey! Good to see you!",
    "Hello! How may I assist you?",
    "Hi, how can I help you today?",
    "Greetings! How may I be of service?",
]

how_are_you_replies = [
    "I'm doing great! Thanks for asking 😄",
    "Functioning at 100% efficiency!",
    "I'm good. How about you?",
    "Doing well, thanks! 😊",
    "All good on my end!",
    "Feeling awesome today!",
    "I'm fine, hope you are too!",
    "Running smoothly 😎",
    "Couldn't be better!",
    "I'm okay and ready to help!",
    "Doing pretty great, actually!",
    "All systems operational 🚀",
    "Feeling helpful as always!",
    "I'm doing well, thanks for checking in!",
    "Just chilling and ready to assist 😄"
]


jokes = [
    "Why did the computer show up at work late? It had a hard drive 😂",
    "I'm reading a book on anti-gravity. It's impossible to put down!",
    "Why don’t programmers like nature? Too many bugs 🐛",
    "Why did the computer catch a cold? It left its Windows open 🪟",
    "Why do Java developers wear glasses? Because they don’t C 👓",
    "Why was the math book sad? It had too many problems 📘",
    "Why did the keyboard break up with the computer? It felt unappreciated ⌨️",
    "Why did the scarecrow get promoted? He was outstanding in his field 🌾",
    "Why did the smartphone need glasses? It lost its contacts 📱",
    "Why did the developer go broke? Because he used up all his cache 💸",
    "Why don’t robots get scared? They have nerves of steel 🤖",
    "Why did the computer go to therapy? It had too many bytes of anxiety 😄",
    "Why was the equal sign so humble? It knew it wasn’t less than or greater than 😌",
    "Why did the laptop sit on the floor? It needed more space 💾"
]


fallback = [
    "I'm not sure I understand 🤔",
    "Could you rephrase that?",
    "Interesting... tell me more!",
    "Sorry, I didn't quite get that 😅",
    "Can you explain that a bit more?",
    "I'm still learning—could you try saying it differently?",
    "Hmm… that went over my head 🤯",
    "I didn’t catch that. Can you repeat?",
    "Could you clarify what you mean?",
    "Let’s try again 😊"
]



# --- Main Response Function ---

# def get_response(user_msg):


#     # Greeting check
#     if user_msg in greetings:
#         return random.choice(greet_replies)


#     # Small talk: "how are you"
#     if "how are you" or "&" in user_msg:
#         return random.choice(how_are_you_replies)

#     # Time request
#     if "time" in user_msg:
#         from datetime import datetime
#         return "The current time is: " + datetime.now().strftime("%I:%M %p")

#     # Joke request
#     if "joke" or "tell me a joke" or "can u tell a joke for me" or "./." in user_msg:
#         return random.choice(jokes)
    
def get_response(user_msg):

    user_words = user_msg.split()

    # Greeting (FIXED)
    if any(word in user_words for word in greetings):
        return random.choice(greet_replies)

    # How are you
    if "how are you" in user_msg:
        return random.choice(how_are_you_replies)

    if "joke"  in user_msg:
        return random.choice(jokes)
    
    if "time" in user_msg:
        from datetime import datetime
        return "The current time is: " + datetime.now().strftime("%I:%M %p")
    

    # Mood detection (smart + unique)
    mood = detect_mood(user_msg)
    if mood == "positive":
        return "I'm glad you're feeling good! 😊"
    elif mood == "negative":
        return "I'm sorry you're feeling like that. I'm here to chat. ❤️"

    # Default fallback
    return random.choice(fallback)
