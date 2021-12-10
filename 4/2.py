from itertools import islice

import numpy as np

FILE = "input"


def main():
    draws_all, boards_all = parse_input()

    boards_wining_last, draws_winning_last = \
        get_last_winning_board_and_draw(boards_all, draws_all)

    draws_winning_last_number = draws_winning_last[-1]

    boards_winning_last_sum = sum_of_unmarked_fields(boards_wining_last, draws_winning_last)

    return boards_winning_last_sum * draws_winning_last_number


def get_last_winning_board_and_draw(boards_all, draws_all):
    """

    :param boards_all: All boards that should be checked
    :param draws_all: All draws that can lead to a board winning
    :return: (The last winning board, The draws that made the last winning board winning)
    """
    boards_winning, draws_winning = get_winning_boards_and_draws(boards_all, draws_all)

    # assure that data is consistent
    last_winning_board_draw_index = max(boards_winning.keys())
    last_winning_draw_draw_index = max(draws_winning.keys())
    assert last_winning_board_draw_index == last_winning_draw_draw_index

    boards_winning_last = boards_winning.get(last_winning_board_draw_index)
    draws_winning_last = draws_winning.get(last_winning_draw_draw_index)

    # There might be more than one last winning board
    if len(boards_winning_last) != 1 and len(draws_winning_last) != 1:
        # This would have to be handled correct...
        raise NotImplementedError

    return boards_winning_last[0], draws_winning_last[0]


def get_winning_boards_and_draws(boards_all, draws_all):
    """
    Get all winning boards and the draws that made those boards win
    
    :param boards_all: All boards that should be checked
    :param draws_all: All draws that can lead to a board winning
    :return: (All winning boards, All the draws that made those boards winning)
    """
    boards_winning = {}
    draws_winning = {}
    for board in boards_all:
        draws = []
        for draw in draws_all:
            draws.append(draw)

            draw_count = len(draws)

            # dont investigate impossible cases
            if draw_count < 5:
                continue

            if is_board_winning(board, draws):
                # create data structure if not available
                if not boards_winning.get(draw_count):
                    boards_winning[draw_count] = []
                    draws_winning[draw_count] = []

                # two independent data structures are probably not the best solution for this
                # but it works ¯\_(ツ)_/¯
                boards_winning[draw_count].append(board)
                draws_winning[draw_count].append(draws)

                break

    return boards_winning, draws_winning


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
    for row in board:
        assert len(set(row)) == 5
        if set(row).issubset(draws):
            return True
    return False


def sum_of_unmarked_fields(board, draws):
    """calculate the sum of all unmarked numbers of a winning board"""

    unmarked = []
    for item in board.flat:
        if item not in draws:
            unmarked.append(item)

    return sum(unmarked)


if __name__ == '__main__':
    print(main())  # 7686
