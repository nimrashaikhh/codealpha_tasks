# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 21:21:08 2026

@author: Nimra
"""


import random

words = ["python", "codealpha", "intern", "computer", "software", "logic"]

secret_word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("Welcome to the Hangman Game!")
print("The word has", len(secret_word), "letters")

while incorrect_guesses < max_attempts:

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Attempts left:", max_attempts - incorrect_guesses)

    if "_" not in display_word:
        print("Yayy! You guessed the word :)")
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Enter a valid letter please")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess!")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")

if incorrect_guesses == max_attempts:
    print("\n The Game is Over")
    print("The correct word was:", secret_word)
