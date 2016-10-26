"""Code Wars Kata.

https://www.codewars.com/kata/stop-gninnips-my-sdrow
"""


def spin_words(sentence):
    output = ''
    newlist = sentence.split()
    for item in newlist:
        length = len(item)
        if length > 4:
            i = 1
            tempstr = ''
            while i <= length:
                tempstr = tempstr + item[-i]
                i += 1
            output = output + tempstr + ' '
        else:
            output = output + item + ' '
    output = output[0:-1]
    return output
