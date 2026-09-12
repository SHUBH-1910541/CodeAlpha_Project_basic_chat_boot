# Simple Rule-Based Chatbot
# B.Tech 1st Year Mini Project
 
def get_response(user_input):
    text = user_input.lower().strip()
 
    if text in ["hello", "hi", "hey"]:
        return "Hi! How can I help you today?"
 
    elif text in ["how are you", "how are you?"]:
        return "I'm fine, thanks! How about you?"
 
    elif text in ["what is your name", "who are you"]:
        return "I'm a simple chatbot made in Python!"
 
    elif text in ["what can you do"]:
        return "I can chat with you using some basic predefined replies."
 
    elif text in ["thank you", "thanks"]:
        return "You're welcome!"
 
    elif text in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Have a nice day!"
 
    else:
        return "Sorry, I didn't understand that. Can you try again?"
 
 
def main():
    print("=" * 45)
    print("       SIMPLE RULE-BASED CHATBOT")
    print("=" * 45)
    print("Type 'bye' or 'exit' to end the chat.\n")
 
    while True:
        user_input = input("You: ")
 
        response = get_response(user_input)
        print("Bot:", response)
 
        if user_input.lower().strip() in ["bye", "goodbye", "exit", "quit"]:
            break
 
 
if __name__ == "__main__":
    main()
 
