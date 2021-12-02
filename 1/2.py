import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv("input", names=["input"])

    df["roling_sum"] = df["input"].rolling(window=3).sum()
    df["shift"] = df["roling_sum"].shift()
    df["increased"] = df["roling_sum"] > df["shift"]

    print(df["increased"].sum())  # 1739
