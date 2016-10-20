"""Code Wars Katas:  String Pyramid.

http://www.codewars.com/kata/string-pyramid
"""


def watch_pyramid_from_the_side(characters):
    """Generate a breath-taking view.

    View is from the side.
    """
    try:
        if characters is None:
            return None
        if len(characters):
            lines_to_print = []
            characters = characters[::-1]
            length = len(characters)
            for i, c in enumerate(characters):
                num_chars_lvl = (2 * i) + 1
                num_spaces_lvl = ((2 * length) - 1) - num_chars_lvl
                print((' ' * (num_spaces_lvl // 2)) + (c * num_chars_lvl) +
                      (' ' * (num_spaces_lvl // 2)))
                lines_to_print.append((' ' * (num_spaces_lvl // 2)) +
                                      (c * num_chars_lvl) +
                                      (' ' * (num_spaces_lvl // 2)))
            return '\n'.join(lines_to_print)
        return characters
    except TypeError:
        return characters


def watch_pyramid_from_above(characters):
    """Breath-taking view from above.

    It's like you can feel the dry air blowing through your hair as you
    are flying above the great pyramid of text.
    """
    def print_line_from_above(chars, length):
        if len(chars) == 1:
            return chars * length
        return chars[:-1] + ((length - 2 * len(chars[:-1])) * chars[-1]) + chars[:-1][::-1]

    def create_list(characters):
        ret_list = []
        for i in range(0, len(characters)):
            ret_list.append(characters[:i + 1])
        return ret_list + ret_list[::-1][1:]

    try:
        if len(characters):
            lines_to_print = []
            layers = create_list(characters)

            for layer in layers:
                lines_to_print.append(print_line_from_above(layer, 2 * len(characters) - 1))
                print(lines_to_print[-1])
            return '\n'.join(lines_to_print)
        return characters
    except TypeError:
        return characters


def count_visible_characters_of_the_pyramid(characters):
    """Count the visible blocks."""
    try:
        if len(characters):
            return (2 * len(characters) - 1) ** 2
        return -1
    except TypeError:
        return -1


def count_all_characters_of_the_pyramid(characters):
    """Count all blocks in the pyramid."""
    try:
        if len(characters):
            sum = 0
            for i in range(1, len(characters) + 1):
                sum += (2 * i - 1) ** 2
            return sum
        return -1
    except TypeError:
        return -1
