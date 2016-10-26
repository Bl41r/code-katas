"""Code Wars Kata.

https://www.codewars.com/kata/credit-card-issuer-checking
"""


def get_issuer(number):
    cc = str(number)
    if cc[0] == '4' and (len(cc) == 13 or len(cc) == 16) :
        return 'VISA'
    elif cc[0:4] == '6011' and len(cc) == 16:
        return 'Discover'
    elif (cc[0:2] == '34' or cc[0:2] == '37') and len(cc) == 15:
        return 'AMEX'
    elif (cc[0:2] == '51' or cc[0:2] == '52' or cc[0:2] == '53' or cc[0:2] == '54' or cc[0:2] == '55') and (len(cc) == 13 or len(cc) == 16):
        return 'Mastercard'
    else:
        return 'Unknown'
