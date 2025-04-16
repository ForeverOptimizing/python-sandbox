# Robert Lowder 01/22/2025
# Lecture 4 Assignment 2 - Frank, Ian and Glen’s Letters
# https://cs50.harvard.edu/python/2022/psets/4/figlet/

import pyfiglet
import sys

def main():
    if len(sys.argv) == 1:
        fig = pyfiglet.Figlet(font='slant')
    elif len(sys.argv) == 3:
        fig = changeFont()
    elif len(sys.argv) == 2:
        sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

    spam = input("Input: ")
    eggs = fig.renderText(spam)
    print(eggs)


def changeFont():
    try:
        print(sys.argv[1])
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            f = pyfiglet.Figlet(font=sys.argv[2])
            return f
        else:
            sys.exit("Invalid usage")
    except pyfiglet.FontNotFound:
        # print("Font not found!")
        sys.exit("Invalid usage: Font not found")


main()
