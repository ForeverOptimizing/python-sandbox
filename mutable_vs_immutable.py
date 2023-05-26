"""
Immtable:
str
int
float
bool
bytes
tuple

Mutable:
list
set
dict
Most 3rd party library data types
"""

# Simple Example

x = (1,2)
x[0] = 1


# Advanced Example

def get_largest_numbers(numbers, n):
    numbers.sort()

    return numbers[-n:]



