import pytest

def test_result():
    """Test length of result."""
    from forbes import oldrich_and_youngest
    assert len(oldrich_and_youngest('forbes_billionaires_2016.json')) == 2

def test_ages():
    """Test valid ages."""
    from forbes import oldrich_and_youngest
    result = oldrich_and_youngest('forbes_billionaires_2016.json')
    assert result[0][0] == 'Phil Knight'
    assert result[1][0] == 'Mark Zuckerberg'