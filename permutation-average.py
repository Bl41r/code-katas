"""Code Wars Kata.

https://www.codewars.com/kata/permutation-average
"""

from itertools import permutations


def permutation_average(n):
    total = 0
    list_nums = map(''.join, permutations(str(n)))
    for num in list_nums:
        total += float(num)
    return int((total / len(list_nums)) + .5)
