"""Test file for proper_parenthetics function in proper_parenthetics.py ."""

import pytest
import proper_parenthetics as p

INPUT_FUNCS = [
    ('()', 0),
    ('()()', 0),
    ('(())', 0),
    ('(()', 1),
    ('())', -1),
    ('(()())(', 1),
    ('(()()))', -1),
    ('', 0),
    ('asdf', 0),
    ('))((', -1),
]


@pytest.mark.parametrize('user_input, expected', INPUT_FUNCS)
def test_proper_parenthetics(user_input, expected):
    """Test the proper_parenthetics function."""
    assert p.proper_parenthetics(user_input) == expected
