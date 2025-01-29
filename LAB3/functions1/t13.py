# 13  | Write a program able to play the "Guess the number"

import random
n = random.randint(1,21)

def game():
    print("Hello! What is your name?")
    name = input("")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.\nTake a guess.")
    g = int(input())
    while g != n:
        if g < n:
            print("\nYour guess is too low.\nTake a guess.")
        else:
            print("\nYour guess is too low.\nTake a guess.")
        g = int(input())
    print(f"Good job, KBTU! You guessed my number in {n} guesses!")

game()