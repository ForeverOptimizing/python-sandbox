# Robert Lowder 04/16/2025
# Lecture 5 Assignment 1 - Testing my twttr
# https://cs50.harvard.edu/python/2022/psets/5/test_twttr/


from twttr import shorten

def test_shorten():
    assert shorten("pop") == "pp"
    assert shorten("lady") == "ldy"




