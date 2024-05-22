# Robert Lowder 5/20/2024
# Lecture 0 Assignment 4 - Einstein
# https://cs50.harvard.edu/python/2022/psets/0/einstein/

# define constants
SPEED_OF_LIGHT = 300000000



# Take input in KG
mass = input("m: ")
# convert string into int
mass = int(mass)
# E = mc^2
energy = mass*SPEED_OF_LIGHT**2
# Output energy in Jules
print(f"E: {energy}")
# print(f"E: {energy}")


