from collections import defaultdict


def main():
    """
    naive implementation, works, but takes ~20 Seconds on my machine
    """
    crabs = parse_input()

    pos_max = max(crabs)

    movement = {}

    for pos in range(pos_max + 1):

        pos_fuel = defaultdict(int)

        for crab in crabs:
            diff = max(crab, pos) - min(crab, pos)
            fuel = sum(range(diff + 1))

            # print(f"move from {crab} to {pos}: {fuel} fuel")
            pos_fuel[pos] += fuel

        # print(pos, sum(pos_fuel.values()))

        movement[pos] = sum(pos_fuel.values())

    print(min(movement.values()))  # 93397632


def parse_input():
    with open("input") as lines:
        for line in lines:
            return [int(x) for x in line.strip().split(sep=",")]


if __name__ == '__main__':
    main()
