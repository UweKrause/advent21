position_player = {
    1: 8,
    2: 7
}

score = {
    1: 0,
    2: 0
}

players = [1, 2]


def main():
    round = 0
    dice_state = 0

    while score[1] < 1000 and score[2] < 1000:

        player = players[dice_state % len(players)]

        progress = []
        for _ in range(3):
            dice_state = next_dice(dice_state, 1)
            round += 1
            progress.append(dice_state)

        steps = sum(progress)

        pos_new = move(position_player[player], steps)

        position_player[player] = pos_new
        score[player] += pos_new

        # print(f"Player {player} rolls {progress}"
        #       f" and moves to space {position_player[player]}"
        #       f" for a total score of {score[player]}")

    looser_points = min(score[1], score[2])

    return looser_points * round


def move(start, steps):
    pos = (start + steps) % 10
    if pos == 0:
        return 10

    return pos


def next_dice(start, steps):
    wrap = 100
    pos = (start + steps) % wrap
    if pos == 0:
        return wrap

    return pos


if __name__ == '__main__':
    print(main())  # 506466
