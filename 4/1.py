from itertools import islice

import numpy as np

FILE = "input"


def main():
    draws_all, boards = parse_input()

    draws = []
    for draw in draws_all:
        draws.append(draw)

        # dont investigate impossible cases
        if len(draws) < 5:
            continue

        for board in boards:
            if is_board_winning(board, draws):
                return draw * sum_of_unmarked_fields(board, draws)


def parse_input():
    """parse input to numbers drawn and boards available"""

    with open(FILE) as lines:

        # first line contains all draws
        draws_all = [int(x) for x in lines.readline().split(sep=",")]

        # extract all the boards from remaining input
        boards = []
        while True:

            rows = []

            # read following lines from input
            # (1 empty line, 5 lines with content)
            for line in islice(lines, 1 + 5):
                rows += [int(i) for i in line.split()]

            if rows:
                assert len(rows) == 5 * 5
                board = np.resize(np.array(rows), (5, 5))
                boards.append(board)
            else:
                # no input left, leave loop
                break

    return draws_all, boards


def is_board_winning(board, draws):
    """
    Checks if a board can win with regard to currently drawn numbers.
    A board wins if all of the numbers of one row or one column are drawn.
    """

    # The rows of a transposed board are the columns of the not transposed board
    return check_rows(board, draws) or check_rows(board.transpose(), draws)


def check_rows(board, draws):
    """
    Checks for the rows of a board, if they are fully drawn.
    If a (complete) row is a subset of the drawn numbers, it was fully drawn.
    """

    # empty array is falsy, filled array is truthy
    return bool([row for row in board if set(row).issubset(draws)])


def sum_of_unmarked_fields(board, draws):
    """calculate the sum of all unmarked numbers of a winning board"""

    return sum([item for item in board.flat if item not in draws])


if __name__ == '__main__':
    print(main())  # 34506
