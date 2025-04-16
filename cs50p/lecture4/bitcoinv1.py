# Robert Lowder 02/02/2025
# Lecture 4 Assignment 6 - Bitcoin Price Index
# https://cs50.harvard.edu/python/2022/psets/4/bitcoin/

import requests
import json
import sys

def main():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        # print(json.dumps(data, indent=2))
        usd_rate = data["bpi"]["USD"]["rate"]
        print(f"Current Bitcoin price in USD: {usd_rate}")
        if len(sys.argv) < 2:
            sys.exit("Too few arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many arguments")
        else:
            amount = float(sys.argv[1])
            total = amount * float(usd_rate)
            print(f"${total}")
    except requests.RequestException:
        sys.exit("Request Exception")



if __name__ == "__main__":
    main()
