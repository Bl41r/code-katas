"""Auto-complete class relying on a modified trie data structure.

original trie: https://github.com/welliam/data-structures/tree/trie-traversal
"""
from trie import Trie


class AutoCompleter():
    """Callable autocomplete class takes a list to create word_list."""

    def __init__(self, word_list, max_completions=5):
        """Initialize the class with a dictionary."""
        self.max_completions = max_completions
        self.word_list = word_list
        self.trie = Trie()
        for word in self.wordlist:
            self.trie.insert(word)

    def __call__(self, word):
        """Return a list of matches that will complete word."""
        return self.trie.traverse(word)
