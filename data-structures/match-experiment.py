# name = input("What is your name? ")




# match name:
#     case "Harry" | "Hermione" | "Ron":
#         print("Gryffindor")
#     case "Draco":
#         print("Slytherin")
#     case _:
#         print("who?")
#         # default code block



name = input("What is your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:  # Wildcard case
        print("who?")
















# This is broken


spam = input("File name: ")
# check if input ends with any filetype name
match spam:
    case spam.endswith(".gif"):
        print("image/gif")
    case spam.endswith(".jpg") | spam.endswith(".jpeg"):
        print("image/jpeg")
    case spam.endswith(".png"):
        print("image/png")
    case spam.endswith(".pdf"):
        print("application/pdf")
    case spam.endswith(".txt"):
        print("text/plain")
    case spam.endswith(".zip"):
        print("application/zip")







# This is also broken


greet = input("Greeting: ")

match greet:
    case greet.startswith("Hello") | greet.startswith("hello"):
        print("$0")
    # case {greet[0] == "H"} | {greet[0] == "h"}:
    # case greet[0] == "H" | greet[0] == "h":
    # case greet[0] == "H" :
    case greet.startswith("H") | greet.startswith("h"):
        print("$20")
    case _:
        print("$100")