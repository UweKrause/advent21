import pandas as pd

FILE = "input"


def main():
    df = pd.read_csv(FILE, names=["direction", "value"], sep=" ")
    grouped = df.groupby(["direction"]).sum()

    up = grouped["value"].get("up", 0)
    down = grouped["value"].get("down", 0)
    forward = grouped["value"].get("forward", 0)

    position_depth = 0 + down - up
    position_horizontal = 0 + forward

    return position_horizontal * position_depth


if __name__ == '__main__':
    print(main())  # 2039256
