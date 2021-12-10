FILE = "input"

days_to_simulate = 256


def main():
    """
    Instead of simulating all the fish,
    this solution just keeps track of the actual number of fish and applies the given rules to them.

    (There is a shorter way to write this, using something like `new_fish := old_fish.pop(0).)
    """

    fish_swarm = parse_input()

    fish_count = {}

    for timer in range(9):
        fish_count[timer] = fish_swarm.count(timer)

    for day in range(1, days_to_simulate + 1):
        fish_count_zeroes = fish_count[0]

        # each other number [1-8] decreases by 1 if it was present at the start of the day
        fish_count[0] = fish_count[1]
        fish_count[1] = fish_count[2]
        fish_count[2] = fish_count[3]
        fish_count[3] = fish_count[4]
        fish_count[4] = fish_count[5]
        fish_count[5] = fish_count[6]
        fish_count[6] = fish_count[7]
        fish_count[7] = fish_count[8]

        # Each day, a 0 becomes a 6 and adds a new 8 to the end of the list
        fish_count[6] += fish_count_zeroes
        fish_count[8] = fish_count_zeroes

        # print(f"day {day}: {sum(fish_count.values())}: {fish_count}")

    return sum(fish_count.values())


def parse_input():
    with open(FILE) as lines:
        for line in lines:
            return [int(x) for x in line.strip().split(sep=",")]


if __name__ == '__main__':
    print(main())  # 1770823541496
