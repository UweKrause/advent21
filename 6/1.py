days_to_simulate = 80


def main():
    state = parse_input()

    for day in range(1, days_to_simulate + 1):
        pos = -1
        for i in state.copy():
            pos += 1
            if i == 0:
                state[pos] = 6
                state.append(8)
            else:
                state[pos] -= 1

        # print(f"after {day} days", state)

    print(len(state))  # 396210


def parse_input():
    with open("input") as lines:
        for line in lines:
            return [int(x) for x in line.strip().split(sep=",")]


if __name__ == '__main__':
    main()
