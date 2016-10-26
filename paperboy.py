"""Code Wars Kata.

https://www.codewars.com/kata/paperboy
"""


def cheapest_quote(n):
    fourtys = n / 40
    n = n % 40
    twentys = n / 20
    n = n % 20
    tens = n / 10
    n = n % 10
    fivers = n / 5
    singles = n % 5

    return round((fourtys * 3.85) + (twentys * 1.93) + (tens * 0.97) + (fivers * 0.49) + (singles * 0.10), 2)
