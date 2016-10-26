"""Code Wars Kata.

https://www.codewars.com/kata/float-or-integer-verifier
"""


def i_or_f(arr):
    try:
        arr = float(arr)
    except ValueError:
        return False
    if type(arr) == int or type(arr) == float:
        return True
