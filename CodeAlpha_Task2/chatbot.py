# basic chatbot project
def chatbot_response(user_input):
    user_input = user_input.lower()  # make case-insensitive

    if user_input in ["hello", "hi", "hey"]:
        return "Hi! How can I help you?"
    elif user_input == "how are you":
        return "I'm fine, thanks! How about you?"
    elif user_input == "bye":
        return "Goodbye! Have a great day!"
    elif user_input == "good morning":
        return "good moring!how can i help you? "
    else:
        return "Sorry, I didn’t understand that."

print("🤖 Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_message = input("You: ")
    response = chatbot_response(user_message)
    print("Chatbot:", response)

    if user_message.lower() == "bye":
        break