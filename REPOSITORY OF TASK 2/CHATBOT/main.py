from chatbot import get_response

def start_chat():
    print("\n🤖 Smart Rule-Based Chatbot")
    print("Type 'bye' to exit.\n")

    while True:
        user = input("You: ").strip().lower()

        if user == "bye":
            print("Bot: Goodbye! Have a great day!")
            break

        reply = get_response(user)
        print("Bot:", reply)

if __name__ == "__main__":
    start_chat()
