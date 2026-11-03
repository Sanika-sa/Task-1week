import re

# Define intent patterns, keywords, and responses
# Each intent has a regular expression pattern and a list of possible responses
INTENTS = [
    {
        "name": "greetings",
        "pattern": r"\b(hi|hello|hey|greetings|good morning|good evening)\b",
        "responses": [
            "Hello! Welcome to your AI internship tasks. How can I help you today?",
            "Hi there! Ready to build some amazing projects?",
            "Hey! What can I assist you with regarding your internship?"
        ]
    },
    {
        "name": "project_info",
        "pattern": r"\b(project|task|internship|weintern|foundations)\b",
        "responses": [
            "This week's focus is on Foundations of Artificial Intelligence, featuring a Neural Network, a Rule-Based Chatbot, and an AI Tic-Tac-Toe game!",
            "You can choose to complete any of the listed AI tasks: a Neural Network from scratch, this Rule-Based Chatbot, or an AI Tic-Tac-Toe game.",
            "Make sure to implement forward propagation, pattern matching, or the Minimax algorithm depending on your chosen project!"
        ]
    },
    {
        "name": "tech_stack",
        "pattern": r"\b(tech stack|python|numpy|matplotlib|regex|libraries)\b",
        "responses": [
            "The recommended tech stack for this chatbot involves Python and Regular Expressions (Regex) / basic NLP.",
            "For the neural network project, you'll use Python, NumPy, and Matplotlib without heavy ML libraries.",
            "Python is versatile enough for all these foundation tasks!"
        ]
    },
    {
        "name": "help",
        "pattern": r"\b(help|assist|support|guide)\b",
        "responses": [
            "I can help you understand project requirements, write regex patterns, or debug your code. Just ask!",
            "Feel free to ask me about project details, tech stacks, or how to implement intent recognition."
        ]
    },
    {
        "name": "goodbye",
        "pattern": r"\b(bye|goodbye|exit|quit|see you)\b",
        "responses": [
            "Goodbye! Good luck with your AI internship tasks!",
            "Bye! Feel free to return if you need help with the next project.",
            "Take care and keep coding!"
        ]
    }
]

# Fallback responses when no pattern matches
FALLBACK_RESPONSES = [
    "I'm not quite sure I understand. Could you rephrase that or ask about the AI projects?",
    "Hmm, that's outside my current topic range. Try asking about the internship tasks, tech stack, or say hello!",
    "I didn't catch that. You can ask me for help or inquire about the project requirements."
]

import random

def get_bot_response(user_input):
    """Matches user input against predefined regex patterns and returns an appropriate response."""
    # Convert input to lowercase for case-insensitive matching
    cleaned_input = user_input.lower().strip()
    
    # Check each intent pattern
    for intent in INTENTS:
        if re.search(intent["pattern"], cleaned_input):
            return random.choice(intent["responses"])
            
    # If no intent matches, return a random fallback response
    return random.choice(FALLBACK_RESPONSES)

def chatbot_cli():
    """Runs the interactive command-line chatbot session."""
    print("=" * 60)
    print("🤖 Welcome to the AI Internship Rule-Based Chatbot!")
    print("Type 'bye', 'exit', or 'quit' to end the conversation.")
    print("=" * 60)
    
    # Initial greeting from the bot
    print("Chatbot: Hello! How can I help you with your AI internship tasks today?\n")
    
    while True:
        try:
            user_input = input("You: ")
            if not user_input.strip():
                continue
                
            # Get response based on rules
            response = get_bot_response(user_input)
            print(f"Chatbot: {response}\n")
            
            # Exit condition
            if re.search(r"\b(bye|goodbye|exit|quit)\b", user_input.lower()):
                break
                
        except (KeyboardInterrupt, EOFError):
            print("\nChatbot: Goodbye! Good luck with your tasks!")
            break

if __name__ == "__main__":
    chatbot_cli()