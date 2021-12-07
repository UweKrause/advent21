from itertools import islice

import numpy as np


def main():
    draws_all, boards = parse_input()

    draws = []
    found = False
    for draw in draws_all:
        draws.append(draw)

        # dont investigate impossible cases
        if len(draws) < 5:
            continue

        for board in boards:
            found = check_board(board, draws)

            if found:
                winner_sum = calculate_score(board, draws)

                print(draw * winner_sum)  # 34506
                break

        if found:
            break


def parse_input():
    """parse input to numbers drawn and boards available"""

    with open("input") as lines:

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


def check_board(board, draws):
    """
    Checks if a board can win with regard to currently drawn numbers.
    A board wins if all of the numbers of one row or one column are drawn.
    """

    # The rows of a transposed board are the columns of the not transposed board
    return check_rows(board, draws) or check_rows(board.transpose(), draws)


def check_rows(board, draws):
    for row in board:
        assert len(set(row)) == 5
        if set(row).issubset(draws):
            return True
    return False


def calculate_score(board, draws):
    """calculate the sum of all unmarked numbers of a winning board"""
    # todo: list comprehension

    unmarked = []
    for item in board.flat:
        if item not in draws:
            unmarked.append(item)

    return sum(unmarked)


if __name__ == '__main__':
    main()
