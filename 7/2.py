import functools
from collections import defaultdict

FILE = "input"


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
            diff = get_diff(crab, pos)
            fuel = calculate_distance(diff)

            # print(f"move from {crab} to {pos}: {fuel} fuel")
            pos_fuel[pos] += fuel

        # print(pos, sum(pos_fuel.values()))

        movement[pos] = sum(pos_fuel.values())

    return min(movement.values())


@functools.cache
def get_diff(crab, pos):
    return max(crab, pos) - min(crab, pos)


@functools.cache
def calculate_distance(diff):
    return sum(range(diff + 1))


def parse_input():
    with open(FILE) as lines:
        for line in lines:
            return [int(x) for x in line.strip().split(sep=",")]


if __name__ == '__main__':
    print(main())  # 93397632
