"""Code Wars Kata.

https://www.codewars.com/kata/get-all-possible-anagrams-from-a-hash
"""


def anagrams(word):
    if len(word) < 2:
        yield word
    else:
        for i, letter in enumerate(word):
            if letter not in word[:i]:
                for j in anagrams(word[:i] + word[i + 1:]):
                    yield j + letter


def get_words(hash_of_letters):
    x = []
    # put all letters in amounts to be used in a list that becomes joined
    for key in hash_of_letters:
        for letter in hash_of_letters[key]:
            x.append(letter * key)
    return sorted(list(anagrams(''.join(x))))
