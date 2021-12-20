"""
Description: This program will simulate a game of rock paper scissors
"""

# Imports the document with all the words and clues on it
import words_and_clues
import random

# Intro
dec = input("Welcome to hangman! Enter 'y' if you need an explantion on how to play!".lower()) == "y"
if dec:
    print("")
    print("The word will be randomly choosen each time, and each time you take a guess for a letter and get it")
    print("wrong the program will give you a clue to the word.")
    print("")
    print("The program will also show you the words you've already used.")
    input("Press enter when your ready to start!")

print("")
print("--------------------------------------------------------------------------------------------------------")
print("")
print("You have 6 guesses.")
num = random.randint(1, 5)
word = words_and_clues.words[num]
if num == 1:
    print("This word has 7 letters, 2 vowels, no spaces.")
elif num == 2:
    print("This word has 8 letters (including spaces), 3 vowels, one space.")
elif num == 3:
    print("This word has 5 letters, 2 vowels, no spaces")
elif num == 4:
    print("This word has 8 letters, 3 vowels, no spaces")
elif num == 5:
    print("This word has 9 letters, 4 vowels, 1 space")
