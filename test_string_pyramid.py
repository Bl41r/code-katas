"""Test module for string pyramid."""

VISIBLE_BLOCKS = [
    ('a', 1),
    ('ab', 9),
    ('abc', 25),
    ('abcd', 49),
]

ALL_BLOCKS = [
    ('a', 1),
    ('ab', 10),
    ('abc', 35),
    ('abcd', 84),
]

FROM_SIDE = [
    ('a', 'a'),
    ('ab', ' b \naaa'),
    ('abc', '  c  \n bbb \naaaaa')
]

FROM_ABOVE = [
    ('a', 'a'),
    ('ab', 'aaa\naba\naaa'),
    ('abc', 'aaaaa\nabbba\nabcba\nabbba\naaaaa')
]


def test_count_all_characters_of_the_pyramid():
    """Test count all chars of the pyramid func."""
    from string_pyramid import count_all_characters_of_the_pyramid
    for case in ALL_BLOCKS:
        assert count_all_characters_of_the_pyramid(case[0]) == case[1]


def test_count_visible_characters_of_the_pyramid():
    """Test count visible chars of the pyramid func."""
    from string_pyramid import count_visible_characters_of_the_pyramid
    for case in VISIBLE_BLOCKS:
        assert count_visible_characters_of_the_pyramid(case[0]) == case[1]


def test_watch_pyramid_from_the_side():
    """Test the side-view."""
    from string_pyramid import watch_pyramid_from_the_side
    for case in FROM_SIDE:
        assert watch_pyramid_from_the_side(case[0]) == case[1]


def test_watch_pyramid_from_above():
    """Test the eagle's eye view."""
    from string_pyramid import watch_pyramid_from_above
    for case in FROM_ABOVE:
        assert watch_pyramid_from_above(case[0]) == case[1]
