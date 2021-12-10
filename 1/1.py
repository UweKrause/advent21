import pandas as pd

FILE = "input"


def main():
    df = pd.read_csv("input", names=[FILE])
    df["shift"] = df["input"].shift()
    df["increased"] = df["input"] > df["shift"]
    return df["increased"].sum()


if __name__ == '__main__':
    print(main())  # 1715
