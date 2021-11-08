
import sys
import random

def menu():
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 to find out the secret number.")
    print("Type 'exit' to end the game.")
    print("Good luck!\n")

def getInput():
    print("What's your guess between 1 and 99?")
    guess = input(">> ")
    return guess

def checkIfMystery(value, mystery, nb_try):
    if value == mystery:
        if mystery == 42:
            print("The answer to the ultimate question of life, the universe and everything is 42.")
        if (nb_try == 1):
            print("Congratulations! You got it on your first try!")
        else:
            print("Congratulations, you've got it!")
            print("You won in {} attempts!".format(nb_try))
        return True
    elif value < mystery:
        print("Too low!")
        return False
    else:
        print("Too high!")
        return False

def checkInput(guess, mystery, nb_try):
    if not checkInt(guess):
        print("That's not a number.")
        return False
    value = (int)(guess)
    if value > 99 or value < 1:
        print("That's not a number between 1 and 99.")
        return False
    if not checkIfMystery(value, mystery, nb_try):
        return False
    return True

def checkInt(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

mystery = random.randint(1, 99)
menu()
nb_try = 0
while True:
    nb_try += 1
    guess = getInput()
    if (guess == "exit"):
        print("Goodbye!")
        break
    elif checkInput(guess, mystery, nb_try):
        break
