# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 22:08:31 2026

@author: Nimra
"""

def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."


def execute_chatbot():
    print("Hey! It's me your personal chatbot.")

    while True:
        user_input = input("User: ")

        response = chatbot_response(user_input)
        print("Chatbot:", response)

        if user_input.lower().strip() == "bye":
            break


# Start chatbot
execute_chatbot()
