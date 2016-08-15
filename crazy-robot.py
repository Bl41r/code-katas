"""Code Wars Kata.

https://www.codewars.com/kata/56a313a0538696bcab000004
"""


def finaldist_crazyrobot(moves, init_pos):
    total_x = 0
    total_y = 0

    for move in moves:
        if move[0] == 'R':
            total_x += move[1]
        elif move[0] == 'L':
            total_x -= move[1]
        elif move[0] == 'U':
            total_y += move[1]
        elif move[0] == 'D':
            total_y -= move[1]

    return ((total_x)**2 + (total_y)**2)**(0.5)
