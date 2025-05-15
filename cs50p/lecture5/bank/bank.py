# Robert Lowder 04/16/2025
# Lecture 5 Assignment 2 - Back to the Bank
# https://cs50.harvard.edu/python/2022/psets/5/test_bank/

def main():
    greeting = input("Greeting: ")
    money = value(greeting)
    print(f"${money}")


def value(greeting):
    if greeting.startswith("Hello") | greeting.startswith("hello"):
        return 0
    elif greeting[0] == "H" :
        return 20
    elif greeting[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()