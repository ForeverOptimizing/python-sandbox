# Robert Lowder 5/20/2024
# Lecture 2 Assignment 2 - Coke Machine
# https://cs50.harvard.edu/python/2022/psets/2/coke/

PRICE = 50

balance = 0
transactionInProgress = True
while transactionInProgress:
    print(f"Amount Due: {PRICE - balance}")
    coin = input("Insert Coin: ")
    match coin:
        case "25":
            balance += 25
        case "10":
            balance += 10
        case "5":
            balance += 5

    if (balance - PRICE) >= 0:
        print(f"Change Owed: {balance - PRICE}")
        transactionInProgress = False
    
