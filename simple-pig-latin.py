"""Code Wars Kata.

https://www.codewars.com/kata/simple-pig-latin
"""


def pig_it(text):
    new_string = ''
    for word in text.split():
        if word.isalpha() == True:
            new_word = ''
            first = word[0:1]
            new_word = word[1:] + first + 'ay '
            new_string += new_word
        else:
            new_string += word + ' '
    new_string = new_string[0:-1]
    return new_string
