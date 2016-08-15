"""Code Wars Kata.

https://www.codewars.com/kata/number-of-permutations-without-repetitions
"""

#from itertools import permutations
import math


def perms(element):
    #return len(set(map(''.join, permutations(str(element)))))
    # apparently the above statement takes too long..so I just
    # calculated the poss permutations based on length and repetition:

    dict1 = {}
    list1 = []
    # put counts for each char in a dict
    for c in str(element):
        if c not in dict1:
            dict1[c] = 1
        else:
            dict1[c] += 1
    b = 1
    for key in dict1:
        if dict1[key] > 1:
            list1.append(dict1[key])
    for item in list1:
        b = b * math.factorial(item)
    return math.factorial(len(str(element))) / b
