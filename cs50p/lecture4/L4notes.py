# Robert Lowder 01/18/2025
# CS50P - Lecture 4 - Libraries
# https://www.youtube.com/watch?v=MztLZWibctI

# importing the entire random module
import random
import cowsay
import requests
import json
import statistics


# has lots of functions that have to do the with the host computer
import sys

from sayings import hello


# importing the specific function from the random module
# this allows you to call the function with choice() rather than random.choice()
# from random import choice

def main():
    coinFlip()
    oneThroughTen()
    deckManipulation()
    average()
    # name()
    # name2()
    # bovineSpeech()
    # trexSpeech()
    itunesSearch()
    hello("world")
    # goodbye("world")

def coinFlip():
    # using the choice function in the random module
    coin = random.choice(["heads", "tails"])
    print(coin)


def oneThroughTen():
    number = random.randint(1, 10)
    print(number)

def deckManipulation():
    # List shuffling demonstration
    cards = ["jack", "queen", "king"]
    random.shuffle(cards)
    for card in cards:
        print(card)


def average():
    # mean function prints the average of the numbers in a given list
    print(statistics.mean([100, 90]))


def name():
    try:
        # will print the name of whatever you type when you execute 'python L4notes.py <your name>'
        print("hello, my name is ", sys.argv[1])
    except IndexError:
        pass


def name2():
    if len(sys.argv) < 2:
        sys.exit("Too few arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many arguments")

    print("hello, my name is ", sys.argv[1])


def name3():
    if len(sys.argv) < 2:
        sys.exit("Too few arguments")

    for arg in sys.argv[1:]:
        print("hello, my name is", arg)


def bovineSpeech():
    if len(sys.argv) == 2:
        cowsay.cow("hello, " + sys.argv[1])

def trexSpeech():
    if len(sys.argv) == 2:
        cowsay.trex("hello, " + sys.argv[1])

def itunesSearch():
    if len(sys.argv) != 2:
        sys.exit()
    response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])
    print(json.dumps(response.json(), indent=2))

    o = response.json()
    for result in o["results"]:
        print(result["trackName"])




main()
