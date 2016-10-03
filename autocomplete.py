"""Auto-complete class relying on a modified trie data structure.

original trie: https://github.com/welliam/data-structures/tree/trie-traversal
"""
from trie import Trie


class AutoCompleter():
    """Callable autocomplete class takes a list to create word_list."""

    def __init__(self, word_list, max_completions=5):
        """Initialize the class with a dictionary."""
        try:
            self.max_completions = int(max_completions)
        except ValueError:
            raise TypeError('max_completions must be an int type.')
        self.word_list = word_list
        self.trie = Trie()
        for word in self.word_list:
            try:
                self.trie.insert(word)
            except TypeError:
                raise TypeError('List contains non-string objects.')

    def __call__(self, word):
        """Return a list of matches that will complete word."""
        return self.trie.traverse(word, self.max_completions)
