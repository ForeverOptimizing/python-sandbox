#   Assignment https://cs50.harvard.edu/python/2022/psets/3/fuel/
#   5/15/2024

import sys


if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")
# elif the string has characters in it?
#     sys.exit("Only numbers please")
else:
    fraction = eval(sys.argv[1])
    percentage = int(100*int(fraction))
    fuel = f"{percentage}%"
    print(type(fuel))
    print(fuel)





