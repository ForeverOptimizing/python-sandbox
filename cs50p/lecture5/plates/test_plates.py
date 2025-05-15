# Robert Lowder 05/15/2025
# Lecture 5 Assignment 3 - Re-requesting a Vanity Plate
# https://cs50.harvard.edu/python/2022/psets/5/test_plates/



from plates import is_valid
# from plates import main
# from plates import midNum
# from plates import twoStart
# from plates import noPunctuation
# from plates import length



def test_is_valid():
    assert is_valid("BINGO") == True
    assert is_valid("BINGO WINGS") == False
    assert is_valid("Hello") == True
    assert is_valid("Hello, World") == False

