# Robert Lowder 5/20/2024
# Lecture 2 Assignment 1 - camelCase
# https://cs50.harvard.edu/python/2022/psets/2/camel/

camel = input("camelCase: ")
snake = ""

for c in camel:
    if c.isupper():
        c = c.lower()
        snake = snake + "_" + c
    else:
        snake = snake + c

print(snake)

