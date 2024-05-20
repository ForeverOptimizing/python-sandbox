# Robert Lowder 5/20/2024
# Lecture 2 Assignment 3 - Just setting up my twttr
# https://cs50.harvard.edu/python/2022/psets/2/twttr/

spam = input("Input: ")
eggs = ""
for c in spam:
    match c:
        case "a":
            pass
        case "e":
            pass
        case "i":
            pass
        case "o":
            pass
        case "u":
            pass
        case _:
            eggs += c


print(eggs)