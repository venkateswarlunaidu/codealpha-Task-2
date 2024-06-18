import nltk
import random
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses for the chatbot
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name?",
        ["My name is Chatbot and I'm here to assist you.",]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm great, thanks for asking!"]
    ],
    [
        r"sorry (.*)",
        ["It's alright, no worries.", "No problem, I understand.",]
    ],
    [
        r"(.*) (hungry|tired|sleepy)",
        ["Take a break and have some rest.", "Why don't you grab a snack?",]
    ],
    [
        r"(.*)\?",
        ["Sorry, I'm just a simple chatbot and may not have all the answers.",]
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye, have a great day!"]
    ],
]

# Create a Chatbot with NLTK
def chatbot():
    print("Hi! I'm a simple chatbot. You can start chatting with me. Type 'quit' to end the conversation.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
