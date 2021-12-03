import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv("example", names=["input"], dtype=str)

    # one column for every character
    df["a"] = df["input"].str[0]
    df["b"] = df["input"].str[1]
    df["c"] = df["input"].str[2]
    df["d"] = df["input"].str[3]
    df["e"] = df["input"].str[4]

    # find the most common value in each column
    a = df["a"].mode()[0]
    b = df["b"].mode()[0]
    c = df["c"].mode()[0]
    d = df["d"].mode()[0]
    e = df["e"].mode()[0]

    # concat the
    bits_most_common = f"{a}{b}{c}{d}{e}"

    # "flip" "bits" (suggestions for solution that actually uses binary welcome!)
    bits_least_common = ''.join('1' if x == '0' else '0' for x in bits_most_common)

    rate_epsilon = int(bits_most_common, 2)
    rate_gamma = int(bits_least_common, 2)

    print(rate_epsilon, rate_gamma, rate_epsilon * rate_gamma)
