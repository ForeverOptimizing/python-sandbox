# Robert Lowder 04/16/2025
# Lecture 5 Assignment 2 - Back to the Bank
# https://cs50.harvard.edu/python/2022/psets/5/test_bank/


from bank import value


def test_value():
    assert value("yo") == 100
    assert value("Hello") == 0
    assert value("hey") == 20
    assert value("hi") == 20
    assert value("howdy") == 20
