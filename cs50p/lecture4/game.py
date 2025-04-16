# Robert Lowder 01/29/2025
# Lecture 4 Assignment 4 - Guessing Game
# https://cs50.harvard.edu/python/2022/psets/4/game/

import random

def main():
    spam = gatherSpam()
    egg = random.choice(range(spam))
    # print(f"num is {egg + 1}")

    guessing = True
    while guessing:
        try:
            guess = input("Guess: ")
            guess = (int(guess) - 1)
            if guess < 0:
                pass
            elif guess == egg:
                print("Just right!")
                guessing = False
            elif guess > egg:
                print("Too large!")
            elif guess < egg:
                print("Too small!")
            else:
                pass
        except ValueError:
            pass


def gatherSpam():
    gathering = True
    while gathering:
        try:
            spam = input("Level: ")
            spam = int(spam)
            if spam < 0: pass
            else: return spam
        except ValueError:
            pass
        except IndexError:
            pass


main()