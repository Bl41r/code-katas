"""Code Wars Kata.

https://www.codewars.com/kata/dna-sequence-tester
"""


def check_DNA(seq1, seq2):

    def invertstrand(seq):
        newseq = ''
        for base in seq:        # convert bases to complimentary base
            if base == 'A':
                newseq += 'T'
            if base == 'T':
                newseq += 'A'
            if base == 'C':
                newseq += 'G'
            if base == 'G':
                newseq += 'C'
        return newseq[::-1]    # reverse order of string for alignment

    invertedseq = invertstrand(seq2)
    if seq1 in invertedseq or invertedseq in seq1:
        return True
    else:
        return False
