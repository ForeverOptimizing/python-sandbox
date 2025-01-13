# CS50P - Lecture 2 - Loops
# https://www.youtube.com/watch?v=-7xg8pGcP6w


def main ():
    number = get_number()
    meow(number)


def get_number():  
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n


def meow(n):
    for _ in range(n):
        print("meow")



main()

