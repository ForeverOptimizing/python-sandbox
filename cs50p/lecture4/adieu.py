# Robert Lowder 01/26/2025
# Lecture 4 Assignment 3 - Adieu, Adieu
# https://cs50.harvard.edu/python/2022/psets/4/adieu/


def main():
    names = obtainNames()
    if len(names) == 1:
        print(f"Adieu, adieu, to {names[0]}")
    if len(names) == 2:
        print(f"Adieu, adieu, to {names[0]} and {names[1]}")
    if len(names) > 2:
        eggs = len(names)
        print("Adieu, adieu, to ", end="")
        for egg in range(eggs):
            if (egg + 1) == eggs:
                print(f"and {names[egg]}", end="")
            else: 
                print(f"{names[egg]}, ", end="")


def obtainNames():
    gathering = True
    names = []
    while gathering:
        try:
            names.append(input("Name: "))
        except EOFError:
            return names


main()