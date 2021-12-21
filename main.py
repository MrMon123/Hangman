"""
Description: This program will simulate a game of rock paper scissors
"""

# Imports the document with all the words and clues on it
import words_and_clues
import random

wrong_letters = []
correct_letters = []
chances = 6
choices = [1, 2, 3, 4, 5, 6]


def checker(numba):
    if chicken:
        print(words_and_clues.chicken_clues[numba])
        choices.remove(numba)
    elif amongus:
        print(words_and_clues.amongus_clues[numba])
        choices.remove(numba)
    elif jesus:
        print(words_and_clues.jesus_clues[numba])
        choices.remove(numba)
    elif computer:
        print(words_and_clues.computer_clues[numba])
        choices.remove(numba)
    elif joebiden:
        print(words_and_clues.joebiden_clues[numba])
        choices.remove(numba)
    else:
        print("ERROR: NO BOOLS SELECTED")

def guess():
    if chicken:
        guess_user = input("Enter your guess: ")
        if guess_user in letters:
            correct_letters.append(guess_user)
            print("That is correct!")
            print("")
            print("Your next clue is;")

        else:
            wrong_letters.append(guess_user)
            print("The letter is not apart of the word. Try again!")
            print("")
            print("You clue is;")
            return "wrong"

# Intro
dec = input("Welcome to hangman! Enter 'y' if you need an explanation on how to play!".lower()) == "y"
if dec:
    print("")
    print("The word will be randomly chosen each time, and each time you take a guess for a letter and get it")
    print("wrong the program will give you a clue to the word.")
    print("")
    print("The program will also show you the words you've already used.")
    input("Press enter when your ready to start!")

# Initialization of the game
print("")
print("--------------------------------------------------------------------------------------------------------")
print("")
print("You have 6 guesses.")
num = random.randint(1, 5)
word = words_and_clues.words[num]
if num == 1:
    print("This word has 7 letters, 2 vowels, no spaces.")
    chicken = True
    letters = ['c', 'h', 'i', 'c', 'k', 'e', 'n']
elif num == 2:
    print("This word has 8 letters (including spaces), 3 vowels, one space.")
    amongus = True
    letters = ['a', 'm', 'o', 'n', 'g', 'u', 's']
elif num == 3:
    print("This word has 5 letters, 2 vowels, no spaces")
    jesus = True
elif num == 4:
    print("This word has 8 letters, 3 vowels, no spaces")
    computer = True
elif num == 5:
    print("This word has 9 letters, 4 vowels, 1 space")
    joebiden = True


while chances > 0:
    run = guess()
    if run == "wrong":
        num = random.randint(1, 6)
        if num in choices:
            numba = num
            checker(numba)
