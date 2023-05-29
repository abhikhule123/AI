import random

responses = {
    "hello": ["Hi!", "Hello!"],
    "goodbye": ["Goodbye!", "See you later!"],
    "thanks": ["You're welcome!"],
    "default": ["I'm sorry, I don't understand."]
}

knowledge_base = {
    "what is your name?":"Buddy",
    "what does a laptop service involve?":" cleaning the internal components, checking for hardware issues",
    "how long a laptop service usually take?":"The duration of a laptop service can vary depending on the specific tasks",
    "how much laptop servicing cost?":" The cost of laptop servicing can vary depending on factors",
    "why is my laptop screen flickering?":" including outdated graphics drivers, incompatible software, or a faulty display cable.",
    "my laptop screen has dead pixels":"caused by physical defects in the screen and cannot be repaired.", 
}

def generate_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return random.choice(responses["hello"])
    elif "goodbye" in user_input:
        return random.choice(responses["goodbye"])
    elif "thank" in user_input:
        return random.choice(responses["thanks"])
    else:
        for question, answer in knowledge_base.items():
            if question in user_input:
                return answer
        return random.choice(responses["default"])

def add_knowledge(question, answer):
    knowledge_base[question.lower()] = answer

while True:
    user_input = input("User: ")
    if user_input.lower() == "add knowledge":
        question = input("Enter a question: ")
        answer = input("Enter the answer: ")
        add_knowledge(question, answer)
        print("Knowledge added successfully!")
    else:
        response = generate_response(user_input)
        print("Chatbot:", response)
