import math

import numpy as np

FILE = "input"


def main():
    heightmap = parse_input()

    points_low = get_points_low(heightmap)

    basins = get_basins(heightmap, points_low)

    return math.prod(get_largest_basins(basins, 3))


def get_largest_basins(basins, n):
    basin_lengths = [len(b) for b in basins]
    basin_lengths.sort(reverse=True)
    return basin_lengths[:n]


def parse_input():
    with open(FILE) as lines:
        rows = 0
        fields = []
        for line in lines:
            rows += 1
            fields += line.strip()

        columns = len(line.strip())

        heightmap = np.array(fields, dtype=int)
        heightmap = heightmap.reshape((rows, columns))

        return heightmap


def get_points_low(heightmap):
    rows, columns = heightmap.shape

    points_low = np.zeros(shape=(rows, columns), dtype=int)
    for r in range(rows):
        for c in range(columns):
            point = (r, c)
            h_point = heightmap[point]
            h_up, h_right, h_down, h_left = get_neighbours_height(heightmap, point)

            if is_point_low(h_point, h_up, h_right, h_down, h_left):
                points_low[point] = 1

    return points_low


def is_point_low(height, height_down, height_left, height_right, height_up):
    return height < height_up \
           and height < height_right \
           and height < height_down \
           and height < height_left


def get_basins(heightmap, points_low):
    basins = []
    for x, y in np.argwhere(points_low):
        basin = set()
        to_check = set()
        to_check.add((x, y))

        # todo: find better way
        while to_check != basin:
            for c in to_check.copy():
                if c is not None and heightmap[c] < 9:
                    basin.add(c)

                    # todo: remove duplicate check
                    for n in get_neighbours(heightmap, c):
                        if n is not None and heightmap[n] < 9:
                            to_check.add(n)

        basins.append(basin)

    return basins


def get_neighbours(heightmap, point):
    rows, columns = heightmap.shape
    x, y = point

    n_up = (x - 1, y) if (0 < x) else None
    n_right = (x, y + 1) if (y < columns - 1) else None
    n_down = (x + 1, y) if (x < rows - 1) else None
    n_left = (x, y - 1) if (0 < y) else None

    return n_up, n_right, n_down, n_left


def get_neighbours_height(heightmap, point):
    n_up, n_right, n_down, n_left = get_neighbours(heightmap, point)

    h_up = heightmap[n_up] if n_up is not None else math.inf
    h_right = heightmap[n_right] if n_right is not None else math.inf
    h_down = heightmap[n_down] if n_down is not None else math.inf
    h_left = heightmap[n_left] if n_left is not None else math.inf

    return h_up, h_right, h_down, h_left


if __name__ == '__main__':
    print(main())  # 900900
