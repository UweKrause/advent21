import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv("input", names=["input"])
    df["shift"] = df["input"].shift()
    df["increased"] = df["input"] > df["shift"]
    print(df["increased"].sum())  # 1715
