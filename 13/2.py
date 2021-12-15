import math

import numpy as np

FILE = "input"

"""
Prints the folded instruction.
Is not really readable, what did I do wrong???

Changes from part 1:
- Dont break after the first fold
- print the result instead of calculate dots
"""


def main():
    dots, folds = parse_input()

    state = create_map(dots)

    state = fold_it(folds, state)

    return state


def parse_input():
    dots = []
    folds = []
    with open(FILE) as lines:
        for line_raw in lines:
            line = line_raw.strip()

            if len(line) == 0:
                continue

            if line.startswith("fold along "):
                folds.append(line[11:])
                continue

            x, y = line.split(",")
            dots.append((int(x), int(y)))

    return dots, folds


def create_map(dots):
    max_x = -math.inf
    max_y = -math.inf

    for x, y in dots:
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    shape = (max_y + 1, max_x + 1)

    a = np.zeros(shape=shape, dtype=bool)

    for x, y in dots:
        a[y][x] = True

    return a


def fold_it(folds, state):
    for fold in folds:
        axis, pos = fold.split("=")

        if axis == "y":
            state = fold_up(state, pos)

        if axis == "x":
            state = fold_left(state, pos)

    return state


def fold_up(arr, pos):
    """folding is keeping the upper half of what you get if you flip the page (up) and stack it onto the original"""

    flip = np.flipud(arr)
    stack = arr + flip

    # return only the upper halve
    return np.split(stack, (0, int(pos)), axis=0)[1]


def fold_left(arr, pos):
    """folding is keeping the left half of what you get if you flip the page (left) and stack it onto the original"""

    flip = np.fliplr(arr)
    stack = arr + flip

    # return only the left halve
    return np.split(stack, (0, int(pos)), axis=1)[1]


if __name__ == '__main__':
    output = main()

    for y in output:
        for x in y:
            if x:
                print("X", end="")
            else:
                print(" ", end="")

        print()
