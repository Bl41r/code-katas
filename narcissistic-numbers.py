"""Code Wars Kata.

https://www.codewars.com/kata/narcissistic-numbers
"""


def is_narcissistic(i):
    n = len(str(i))
    total = 0
    for c in str(i):
        total = int(c)**n + total
    if total == i:
        return True
    else:
        return False
