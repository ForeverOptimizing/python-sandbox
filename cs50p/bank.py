# Lecture 1 Assignment 2
# Robert Lowder 5/20/2024
# https://cs50.harvard.edu/python/2022/psets/1/bank/

greet = input("Greeting: ")

match greet:
    case greet.startswith("Hello") | greet.startswith("hello"):
        print("$0")
    # case greet[0] == "H" | greet[0] == "h":
    case greet[0] == "H" :
        print("$20")
    case _:
        print("$100")


# if greet.startswith("Hello"):
#     print("$0")
# elif greet.startswith("hello"):
#     print("$0")
# elif greet[0] == "H":
#     print("$20")
# elif greet[0] == "h":
#     print("$20")
# else:
#     print("$100")