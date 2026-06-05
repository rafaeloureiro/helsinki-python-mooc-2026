"""
Non transitive dice play game.
"""

from random import choice

def roll(die: str) -> int:

    dice01 = (3, 3, 3, 3, 3, 6)
    dice02 = (2, 2, 2, 5, 5, 5)
    dice03 = (1, 4, 4, 4, 4, 4)

    if die == 'A':
        return choice(dice01)
    elif die == 'B':
        return choice(dice02)
    elif die == 'C':
        return choice(dice03)
    else:
        raise ValueError('die must be one of: A, B, C')


def play(die1: str, die2: str, times: int) -> tuple:

    wins1 = 0
    wins2 = 0
    ties = 0

    for _ in range(times):
        result1 = roll(die1)
        result2 = roll(die2)

        if result1 > result2:
            wins1 += 1
        elif result2 > result1:
            wins2 += 1
        else:
            ties += 1

    return wins1, wins2, ties

