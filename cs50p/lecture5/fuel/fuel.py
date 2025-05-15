# Robert Lowder 05/15/2025
# Lecture 5 Assignment 4 - Refueling
# https://cs50.harvard.edu/python/2022/psets/5/test_fuel/


def main():
    # get string input
    thisFraction = input("Fraction: ")
    # send string to convert
    thisPercentage = convert(thisFraction)
    reading = gauge(thisPercentage)
    print(reading)



def convert(fraction):
    # expects a str in X/Y format as input
    # derive x from string
    try:
        x, y = map(int, fraction.split('/'))

    except ValueError:
        print("ValueError")
    # derive y from string

    # if x and y are integers raise ValueError
    # if x is greater than y raise ValueError
    # if y is equal to 0 raise ZeroDivisionError
    # returns that fraction as a percentage rounded to the nearest int between 0 and 100 
    ...


def gauge(percentage):
    # expects an int and returns a string
    # "E" if that int is less than or equal to 1,
    # "F" if that int is greater than or equal to 99,
    # and "Z%" otherwise, wherein Z is that same int.

    ...


if __name__ == "__main__":
    main()