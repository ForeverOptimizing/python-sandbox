# Robert Lowder 04/16/2025
# Lecture 4 Assignment 6 - Bitcoin Price Index
# https://cs50.harvard.edu/python/2022/psets/4/bitcoin/

import requests
import sys
import json


# "rest.coincap.io/v3/assets/bitcoin?apiKey=8ec1189320bd9fdd881c244b5bd4b786b8e5b7b09e4416cdd09950043a6a354c"

try:
    # "Missing command-line argument"
    if len(sys.argv) == 1: sys.exit("Missing command-line argument")
    # Coins defined
    elif len(sys.argv) == 2: coins = float(sys.argv[1])
    # "Too many Command-line arguments"
    elif len(sys.argv) > 3: sys.exit("Too many Command-line arguments")

    # Access API
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=8ec1189320bd9fdd881c244b5bd4b786b8e5b7b09e4416cdd09950043a6a354c")
    response = response.json()
        # print(response.json())
        # print(json.dumps(response, indent=1))
    # Get bitcoin Price
    price = response['data']['priceUsd']
    # Multiply Price by coins
    total = float(price) * float(coins)
    # Print total formatted to 4 decimal places and a , for the thousands
    print(f"${total:,.4f}")

except requests.RequestException:
    sys.exit("Request exception")
# "Command-line argument is not a number"
except ValueError:
    sys.exit("Command-line argument is not a number")


# {'data': {
#     'id': 'bitcoin', 
#     'rank': '1', 
#     'symbol': 'BTC', 
#     'name': 'Bitcoin', 
#     'supply': '19850321.0000000000000000', 
#     'maxSupply': '21000000.0000000000000000', 
#     'marketCapUsd': '1699274252622.0060085884653821', 
#     'volumeUsd24Hr': '9473385435.6806725349689578', 
#     'priceUsd': '85604.3714669403083501', 
#     'changePercent24Hr': '2.0305817776205623', 
#     'vwap24Hr': '84041.8642724797547040', 
#     'explorer': 'https://blockchain.info/'}, 
#     'timestamp': 1744490909359}