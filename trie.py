"""Implement Trie data structure."""


class Trie(object):
    """Trie data structure."""
    def __init__(self):
        self.words = {}

    def contains(self, s):
        """Return whether a string is contained within the trie."""
        words = self.words
        for c in s:
            if c == '$' or c not in words:
                return False
            words = words[c]
        return words.get('$', False)

    def insert(self, s):
        """Insert string into trie."""
        words = self.words
        if '$' in s:
            raise ValueError('String inserted into trie must not contain $.')
        for c in s:
            words = words.setdefault(c, {})
        words['$'] = True

    def traverse(self, start_word):
        """Traverse the trie depth-first (pre order)."""
        words = self.words
        autocomplete_words = []

        for c in start_word:
            words = words[c]

        stack = [(words, '')]
        while len(stack):
            d, word = stack.pop()
            if '$' in d:
                autocomplete_words.append(start_word + word)
                print(start_word + word)
            for c in d:
                if c != '$':
                    stack.append((d[c], word + c))

        return autocomplete_words
