# Robert Lowder 01/29/2025
# Lecture 4 Assignment 5 - Little Professor
# https://cs50.harvard.edu/python/2022/psets/4/professor/

import random


def main():
    STRIKE_LIMIT = 3
    strikes = 0
    score = 0
    level = get_level()
    # failure = False




    for question in range(10):
        # if failure == True: continue
        x = generate_integer(level)
        y = generate_integer(level)
        egg = x + y
        answering = True
        # GameOver = False
        print(x, y, egg) # for testing purposes   
        while answering:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == egg: 
                    score = score + 1
                    strikes = 0
                    answering = False
                else:
                    strikes = strikes + 1
                    print("EEE")
                    if strikes == STRIKE_LIMIT: 
                        strikes = 0
                        answering = False
 
                        
            except ValueError:
                strikes = strikes + 1
                print("EEE")
                if strikes == STRIKE_LIMIT: 
                    strikes = 0
                    answering = False

    print(f"SCORE: {score}")




def get_level():
    gathering = True
    while gathering:
        try:
            level = input("Level: ")
            level = int(level)
            if level not in range(1,3):
                ...
            else: return level

        except ValueError:
            pass


def generate_integer(level):
    if level == 1: return random.choice(range(1,10))
    if level == 2: return random.choice(range(1,100))
    if level == 3: return random.choice(range(1,1000))



if __name__ == "__main__":
    main()