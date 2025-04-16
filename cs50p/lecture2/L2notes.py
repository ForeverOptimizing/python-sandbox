# CS50P - Lecture 2 - Loops
# https://www.youtube.com/watch?v=-7xg8pGcP6w





# == Mario.py ==

def main():
    print_row(4)
    print_column(3)
    print_square(3)


def print_square(size):
    # For each row in square
    for i in range(size):

        # For each brick in row
        for j in range(size):

            # Print brick
            print("#", end="")

        # New line for next row
        print()


def print_row(width):
    print("?" * width)

def print_column(height):
    print("#\n" * height, end="")

main()

# for _ in range(3):
#     print("#")




















# == List of Dictionaries Example ==

# students = [
#     {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
#     {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
#     {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel terrier"},
#     {"name": "Draco", "house": "Slytherin", "patronus": None}
# ]

# for student in students:
#     print(student["name"], student["house"], student["patronus"], sep=", ")


# == Second Demonstration ==

# students = ["Hermione", "Harry", "Ron"]

# for student in students:
#     print(student)


# == First Demonstration ==

# def main ():
#     number = get_number()
#     meow(number)

# def get_number():  
#     while True:
#         n = int(input("What's n? "))
#         if n > 0:
#             break
#     return n

# def meow(n):
#     for _ in range(n):
#         print("meow")

# main()




