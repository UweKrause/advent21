import functools
from collections import defaultdict  # <3

players = [1, 2]

position_on_board = {
    1: 8,
    2: 7,
}

SCORE_CAP = 1000
DICE_THROWS_PER_ROUND = 3

score = defaultdict(int)

# initially score for one player.
# Will grow for the other players
score[1] = 0


def main():
    round = 0
    dice_state = 0

    while max(score.values()) < SCORE_CAP:

        player = current_player(round)

        dice_throws = []
        for _ in range(DICE_THROWS_PER_ROUND):
            round += 1
            dice_state = next_dice(dice_state)
            dice_throws.append(dice_state)

        steps = sum(dice_throws)

        position_on_board[player] = move(position_on_board[player], steps)

        score[player] += position_on_board[player]

        # print(f"Player {player} rolls {dice_throws}"
        #       f" and moves to space {position_on_board[player]}"
        #       f" for a total score of {score[player]}")

    return min(score[1], score[2]) * round


def current_player(round):
    return int(wrap(round / DICE_THROWS_PER_ROUND, 1, len(players)))


@functools.cache  # although not necessary, doesnt hurt
def move(start, steps):
    return wrap(start, steps, 10)


def next_dice(start):
    return wrap(start, 1, 100)


def wrap(start, steps, where_to_wrap):
    """
    Performs the modulo-operation different:
    If the remainder is 0, return the end of the allowed range.
    (I am open to better suggestions)
    """
    value = (start + steps) % where_to_wrap
    return where_to_wrap if value == 0 else value


if __name__ == '__main__':
    print(main())  # 506466
