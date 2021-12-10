import pandas as pd

FILE = "input"


def main():
    df = pd.read_csv(FILE, names=["direction", "value"], sep=" ")

    aim = 0
    position_horizontal = 0
    position_depth = 0

    for direction, value in zip(df['direction'], df['value']):

        if direction == "down":
            aim += value

        if direction == "up":
            aim -= value

        if direction == "forward":
            position_horizontal += value
            position_depth += aim * value

    return position_horizontal * position_depth


if __name__ == '__main__':
    print(main())  # 1856459736
