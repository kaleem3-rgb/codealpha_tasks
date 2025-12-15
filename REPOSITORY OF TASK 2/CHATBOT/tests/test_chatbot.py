# tests/test_chatbot.py

from chatbot import get_response
from utils import detect_mood

def test_greeting():
    reply = get_response("hello")
    assert isinstance(reply, str)

def test_mood_positive():
    assert detect_mood("I feel great") == "positive"

def test_mood_negative():
    assert detect_mood("I am sad today") == "negative"

def test_fallback():
    reply = get_response("something random here")
    assert isinstance(reply, str)
