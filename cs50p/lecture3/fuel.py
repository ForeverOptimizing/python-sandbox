# Robert Lowder 05/15/2024 - Revised 01/16/2025
# Lecture 3 Assignment 1 - Fuel Gauge
# https://cs50.harvard.edu/python/2022/psets/3/fuel/


def main():
    printer(getFraction())

def getFraction():
    checking = True
    while checking:
        try:
            fraction = input("Fraction: ")
            num, den = fraction.split("/")
            if int(num) > int(den): continue
            percent = int(int(num)/int(den) * 100)
            return percent
        except ValueError:
             pass
        except ZeroDivisionError:
            pass


def printer(percent):
    if percent <= 1: print("E")
    elif percent >= 99: print("F")
    else: print(f"{percent}%")

main()












# 5/20/2024 Implementation
# checking = True
# while checking:
    
#     fraction = input("Fraction: ")
#     num, den = fraction.split("/")
#     numDeci = num.count(".")
#     denDeci = den.count(".")
#     if numDeci > 0  | denDeci > 0:
#         pass
#     if num.isdigit() & den.isdigit():
#         num = int(num)
#         den = int(den)
#         percent = num / den * 100

#         if (percent >= 99) & (percent <= 100):
#             print("F")
#             checking = False
#         elif (percent >= 0) & (percent <= 1):
#             print("E")
#             checking = False
#         elif (percent < 0) | (percent > 100):
#             pass
#         elif num == 0:
#             pass
#         else:
#             percent = int(percent)
#             print(f"{percent}%")
#             checking = False




































# 5/15/2024 Implementation


# import sys


# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")
# # elif the string has characters in it?
# #     sys.exit("Only numbers please")
# else:
#     fraction = eval(sys.argv[1])
#     percentage = int(100*int(fraction))
#     fuel = f"{percentage}%"
#     print(type(fuel))
#     print(fuel)





