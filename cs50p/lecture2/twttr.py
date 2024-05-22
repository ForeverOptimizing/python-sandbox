# Robert Lowder 5/20/2024
# Lecture 2 Assignment 3 - Just setting up my twttr
# https://cs50.harvard.edu/python/2022/psets/2/twttr/

spam = input("Input: ")
# spam = spam.lower()
eggs = ""
for c in spam:
    match c:
        case "a" | "A":
            pass
        case "e" | "E":
            pass
        case "i" | "I":
            pass
        case "o" | "O":
            pass
        case "u" | "U":
            pass
        case _:
            eggs += c


print(eggs)