# Robert Lowder 5/20/2024
# Lecture 0 Assignment 5 - Tip Calculator
# https://cs50.harvard.edu/python/2022/psets/0/tip/

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = d.replace("$", "")
    d = float(d)
    return d


def percent_to_float(p):
    p = p.replace("%", "")
    p = int(p)/100
    return p


main()
