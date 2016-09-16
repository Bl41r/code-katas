import pytest


def test_result():
    """Test length of result."""
    from forbes import oldrich_and_youngest
    assert len(oldrich_and_youngest('forbes_billionaires_2016.json')) == 2


def test_correct_answers():
    """Test the expected answer.  May fail if json file tampered with."""
    from forbes import oldrich_and_youngest
    result = oldrich_and_youngest('forbes_billionaires_2016.json')
    assert result[0][0] == 'Phil Knight'
    assert result[1][0] == 'Mark Zuckerberg'


def test_data_types():
    """Test data types of result."""
    string = u'hello'
    from forbes import oldrich_and_youngest
    result = oldrich_and_youngest('forbes_billionaires_2016.json')
    assert type(result[0][0]) is type(string)
    assert type(result[0][1]) is int
    assert type(result[0][2]) is type(string)

    assert type(result[1][0]) is type(string)
    assert type(result[1][1]) is int
    assert type(result[1][2]) is type(string)


def test_richness():
    """Test that they are actually worth at least 1 billion USD."""
    from forbes import oldrich_and_youngest
    result = oldrich_and_youngest('forbes_billionaires_2016.json')
    assert result[0][1] >= 1000000000
    assert result[1][1] >= 1000000000
