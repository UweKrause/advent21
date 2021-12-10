import pandas as pd

FILE = "input"


def main():
    df = pd.read_csv("input", names=[FILE])

    df["roling_sum"] = df["input"].rolling(window=3).sum()
    df["shift"] = df["roling_sum"].shift()
    df["increased"] = df["roling_sum"] > df["shift"]

    return df["increased"].sum()


if __name__ == '__main__':
    print(main())  # 1739
