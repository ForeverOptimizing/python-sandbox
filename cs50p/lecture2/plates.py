# Robert Lowder 5/20/2024
# Lecture 2 Assignment 4 - Vanity Plates
# https://cs50.harvard.edu/python/2022/psets/2/plates/


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if noPunctuation(s):
        pass
        # print("noPunctuation SUCCESS")
    else:
        # print("noPunctuation FAILURE")
        return False
    if length(s):
        pass
        # print("length SUCCESS")
    else:
        # print("length FAILURE")
        return False
    if twoStart(s):
        pass
        # print("twoStart SUCCESS")
    else:
        # print("twoStart FAILURE")
        return False
    if midNum(s):
        pass
        # print("midNum SUCCESS")
    else:
        # print("midNum FAILURE")
        return False
    

    return True


def midNum(s):
    numLock = False
    i = 0
    for char in s:
        if i < 3:
            pass
        elif char.isdigit():
            numLock = True
        elif char.isalpha() & numLock:
            return False
        i += 1
    return True
        


def twoStart(s):
    i = 0
    for c in s:
        if i == 2:
            return True
        if c.isalpha():
            pass
        else:
            return False
        i += 1

def noPunctuation(s):
    for c in s:
        if c.isdigit() | c.isalpha():
            pass
        else:
            return False
    return True


def length(s):
    if len(s) < 2:
        return False
    
    if len(s) > 6:
        return False
    
    return True




main()