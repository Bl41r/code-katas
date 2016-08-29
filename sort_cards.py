"""Code Wars Kata.

https://www.codewars.com/kata/sort-deck-of-cards/train/python
"""


def sort_cards(cards):
    """Sort shuffled list of cards, sorted by rank.
    >>> sort_cards(['3', '9', 'A', '5', 'T', '8', '2', '4', 'Q', '7', 'J', '6', 'K'])
    ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    """

    def getkey(item):
        rank = {'A': 1, 'T': 10, 'J': 11, 'Q': 12, 'K': 13}
        try:
            return int(item)
        except ValueError:
            return rank[item]

    return sorted(cards, key=getkey)
