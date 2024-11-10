def chatbot():
# Greeting message

    print("Bot: Hello Navya! I'm your simple chatbot.")
    print("Bot: You can ask me things like 'hello', 'my name', 'help', 'weather', or 'bye'.")

    # Start a loop to continuously interact with the user
    while True:
        user_input = input("You: ").lower()  # Take user input and convert to lowercase
        
        # Rule-based responses using if-else statements
        if "hello" in user_input:
            print("Bot: Hi Navya! How can I assist you today?")
        if "what is your name?" in user_input:
            print("Bot: I'm your Rule-Based Chatbot!")
        elif "how are you?" in user_input:
            print("Bot: I'm just a program, but I'm functioning well!")
        elif "help" in user_input:
            print("Bot: I'm here to help! You can ask me about the weather, a joke, or say goodbye.")
        elif "weather" in user_input:
            print("Bot: Sorry, I can't check live weather right now, but it seems like a great day!")
        elif "joke" in user_input:
            print("Bot: Why did the chicken join a band? Because it had the drumsticks!")
        elif "bye" in user_input:
            print("Bot: Goodbye! Have a great day ahead!")
            break  # Exit the loop if the user says 'bye'
        else:
            print("Bot: I didn't understand that. Could you try asking something else?")

# Entry point for the chatbot
if __name__ == "__main__":
    chatbot()
