"""Code Wars Kata.

https://www.codewars.com/kata/random-case
"""


import random

def random_case(x):
    newstr = ''
    for c in x:
        r = random.randint(0, 1)
        if r == 1:
            newstr += c.swapcase()
        else:
            newstr += c
    return newstr
