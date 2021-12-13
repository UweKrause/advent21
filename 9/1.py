import numpy as np

FILE = "input"


def main():
    heightmap = parse_input()

    points_low = get_points_low(heightmap)

    risk_level = get_risk_level(heightmap, points_low)

    return risk_level


def parse_input():
    with open(FILE) as lines:
        rows = 0
        fields = []
        for line in lines:
            rows += 1
            fields += line.strip()

        columns = len(line.strip())

        a = np.array(fields, dtype=int)
        a = a.reshape((rows, columns))

        return a


def get_points_low(heightmap):
    rows, columns = heightmap.shape
    points_low = np.zeros(shape=(rows, columns), dtype=int)
    for r in range(rows):
        for c in range(columns):
            height = int(heightmap[r, c])

            height_left = int(heightmap[r, c - 1]) if (0 < c) else 9
            height_right = heightmap[r, c + 1] if (c < columns - 1) else 9
            height_up = heightmap[r - 1, c] if (0 < r) else 9
            height_down = heightmap[r + 1, c] if (r < rows - 1) else 9

            if height < height_left and height < height_right and height < height_up and height < height_down:
                points_low[r, c] = 1

    return points_low


def get_risk_level(heightmap, points_low):
    risk_level = 0
    for x, y in zip(heightmap.flat, points_low.flat):
        if y > 0:
            risk_level += x + y
    return risk_level


if __name__ == '__main__':
    print(main())  # 439
