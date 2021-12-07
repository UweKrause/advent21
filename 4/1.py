from itertools import islice
from pprint import pprint

import numpy as np

if __name__ == '__main__':

    draws_all = []
    boards = []

    # parse input to numbers drawn and boards available
    with open("input") as lines:

        # first line gets special treatment
        for line in islice(lines, 1):
            draws_all += [int(x) for x in line.strip().split(sep=",")]

        # Skip 1 empty line of input
        _ = lines.readline()

        # extract all the boards from remaining input
        while True:
            rows = []

            # read following 5 lines from input
            for line in islice(lines, 5):
                rows += [int(i) for i in line.strip().split()]

            # construct board
            if rows:
                assert len(rows) == 5 * 5
                board = np.array(rows)
                board.resize((5, 5))
                boards.append(board)

            # no input left, leave loop
            else:
                break

            # Skip 1 line
            _ = lines.readline()

    draws = []
    found = False
    for draw in draws_all:
        draws.append(draw)

        # dont investigate impossible cases
        if len(draws) < 5:
            continue

        for board in boards:

            for row in board:
                assert len(set(row)) == 5
                if set(row).issubset(draws):
                    found = True

            for col in board.transpose():
                assert len(set(col)) == 5
                if set(col).issubset(draws):
                    found = True

            if found:
                pprint(board)
                print(draw, draws)

                # calculate the sum of all unmarked numbers of the winning board
                unmarked = []
                for item in board.flat:
                    if item not in draws:
                        unmarked.append(item)

                winner_sum = sum(unmarked)

                print(draw * winner_sum)  # 34506

                break

        if found:
            break
