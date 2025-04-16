# Robert Lowder 01/22/2025
# Lecture 4 Assignment 1 - Emojize
# https://cs50.harvard.edu/python/2022/psets/4/emojize/


import emoji


def main():
    spam = input("INPUT: ")
    print(f"OUTPUT: "+ emoji.emojize(spam))




main()