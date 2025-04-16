# Robert Lowder 01/16/2025
# Lecture 3 Assignment 2 - Felipe’s Taqueria
# https://cs50.harvard.edu/python/2022/psets/3/taqueria/



menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

TOTAL = 0

def main():
    global TOTAL
    ordering = True
    while ordering:
        try:
            adder(server())
        except EOFError:
            break


def server():
    ordering = True
    while ordering:
        try:
            order = input("Item: ")
            return menu[order.title()]
        except KeyError:
            pass

def adder(num):
    global TOTAL
    TOTAL = TOTAL + num
    print(f"${TOTAL:.2f}")

main()

