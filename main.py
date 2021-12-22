"""
Description: This program will simulate a game of rock paper scissors
"""

# Imports the document with all the words and clues on it
import words_and_clues
import random

# Sets up the needed variables
wrong_letters = []
correct_letters = []
chances = 6
choices = [1, 2, 3, 4, 5, 6]

# The function that will allow the user to guess and return if it was right or wrong
def guess():
    guess_user = input("Enter your guess: ")
    # Correct Response
    if guess_user in letters:
        correct_letters.append(guess_user)
        print("That is correct!")
        print("")
        print("Your next clue is;")
        return "correct"
    # Incorrect response
    else:
        wrong_letters.append(guess_user)
        print("The letter is not apart of the word. Try again!")
        print("")
        print("You clue is;")
        return "wrong"

# Intro
dec = input("Welcome to hangman! Enter 'y' if you need an explanation on how to play! ".lower()) == "y"
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

# Checks which word it got and assigns letters
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
        chances -= 1
        choice = random.choice(choices)
        choices.remove(choice)
        if chicken:
            print(words_and_clues.chicken_clues[choice])
        elif amongus:
            print(words_and_clues.amongus_clues[choice])
        elif jesus:
            print(words_and_clues.jesus_clues[choice])
        elif computer:
            print(words_and_clues.computer_clues[choice])
        elif joebiden:
            print(words_and_clues.joebiden_clues[choice])
        else:
            print("ERROR: No selected word found or clue")
