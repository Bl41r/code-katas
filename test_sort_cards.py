import sort_cards


def test_sort_cards():
    """Test kata sorting function."""
    assert sort_cards(list('39A5T824Q7J6K')) == list('A23456789TJQK')
    assert sort_cards(list('Q286JK395A47T')) == list('A23456789TJQK')
    assert sort_cards(list('54TQKJ69327A8')) == list('A23456789TJQK')
