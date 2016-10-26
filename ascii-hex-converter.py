"""Code Wars Kata.

https://www.codewars.com/kata/ascii-hex-converter
"""


class Converter():

    @staticmethod
    def to_ascii(h):
        return h.decode('hex')

    @staticmethod
    def to_hex(s):
        return s.encode('hex')
