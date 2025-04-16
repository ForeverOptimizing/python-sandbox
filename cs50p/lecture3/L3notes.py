# Exceptions LEcture

def main():
    # hello()
    x = get_int("What's x? ")
    print(f"x is {x}")


def hello():
    print("hello, world")


def get_int(prompt):
    gettingInteger = True
    while gettingInteger:
        try:
            return int(input(prompt))
        except ValueError:
            print("x is not an integer")
            # pass
        # else:



main()