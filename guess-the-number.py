#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def set_number():
    return random.randint(1, 100)


def set_difficulty(difficalty):
    if difficalty == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")
        return -1


def game():
    answer = set_number()
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficalty = input("Choose a difficalty. Type 'easy' or 'hard': ")
    turns = set_difficulty(difficalty)
    while turns > 0:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)

    if turns == 0:
        print(f"You've run out of guesses, you lose. The answer was {answer}")
        return


game()
