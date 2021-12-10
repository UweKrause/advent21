import pandas as pd

FILE = "input"

if __name__ == '__main__':
    df = pd.read_csv(FILE, names=["input"], dtype=str)

    col_length = len(df["input"][0])

    # add one column for every character
    for pos_str in range(col_length):
        df[pos_str] = df["input"].str[pos_str]

    # find the most common bit in each column and add it to the string containing the most common bits
    bits_most_common = ""
    for pos_str in range(col_length):
        bits_most_common += df[pos_str].mode()[0]

    # "flip" "bits"
    bits_least_common = ''.join('1' if x == '0' else '0' for x in bits_most_common)

    rate_epsilon = int(bits_most_common, 2)
    rate_gamma = int(bits_least_common, 2)

    power_consumption = rate_epsilon * rate_gamma

    print(power_consumption)  # 2498354
