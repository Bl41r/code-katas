"""Code Wars Kata.

http://www.codewars.com/kata/sum-of-the-first-nth-term-of-series/train/python
"""


def series_sum(n):
    sum_ = 0.00
    for i in range(1, n + 1):
        sum_ += (1.0 / (1 + 3 * (i - 1)))
    return '%.2f' % sum_
