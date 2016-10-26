"""Code Wars Kata.

https://www.codewars.com/kata/braking-well
"""


def dist(v, mu):    # suppose reaction time is 1
    s = .27777777 * v
    return (s + (s**2 / (2 * mu * 9.81)))


def speed(d, mu):                 # suppose reaction time is 1
    # use quadratic eq to solve
    a = 1 / (2 * mu * 9.81)
    return ((-1 + (1 - (-4 * a * d)) ** 0.5) / (2 * a)) * 3.6
