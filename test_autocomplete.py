"""Test module for AutoCompleter class."""

import pytest

TEST_WORDS = ['hell', 'hella', 'hellacious', 'hello', 'hellish', 'hellbound', 'hellion', 'heckle', 'heckler']

def setup_autocompleter(num_results=5):
    from autocomplete import AutoCompleter
    a = AutoCompleter(TEST_WORDS, num_results)
    return a

def test_num_results():
    a = setup_autocompleter()
    results = a('he')
    assert len(results) == 5
    a.max_completions = 2
    results = a('he')
    assert len(results) == 2

def test_result_words():
    a = setup_autocompleter()
    results = a('heckle')
    assert 'heckle' in results
    assert 'heckler' in results
    assert len(results) == 2

def test_init_types():
    from autocomplete import AutoCompleter
    with pytest.raises(TypeError):
        AutoCompleter([3, 'hello'])
    with pytest.raises(TypeError):
        AutoCompleter(TEST_WORDS, 'a')
