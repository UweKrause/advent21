import re

import numpy as np


def main():
    highest_x, highest_y, vents = parse_input()

    # construct empty map
    field = np.zeros((highest_x + 1, highest_y + 1), dtype=int)

    # mark the vents on the map
    for vent in vents:
        for x, y in vent:
            field[x][y] += 1

    # print(field.transpose())

    cells_with_more_than_one_vent = np.count_nonzero(field > 1)

    print(cells_with_more_than_one_vent)


def parse_input():
    highest_x = 0
    highest_y = 0
    vents = []

    with open("input") as lines:
        for line in lines:
            regex = re.compile(r'(\d+),(\d+)+ -> (\d+)+,(\d+)+')
            regex_groups = regex.search(line.strip())
            coords = \
                (point1, point2) = \
                ((x1, y1), (x2, y2)) = \
                (
                    (int(regex_groups.group(1)), int(regex_groups.group(2))),
                    (int(regex_groups.group(3)), int(regex_groups.group(4)))
                )

            # "For now, only consider horizontal and vertical lines"
            if not (x1 == x2 or y1 == y2):
                continue

            # extract max x and max y values to later determine the size of map
            highest_x, highest_y = highest(highest_x, highest_y, x1, x2, y1, y2)

            # take care of the direction of the line
            stride_1 = 1 if x1 <= x2 else -1
            stride_2 = 1 if y1 <= y2 else -1

            # append the points to the vent
            vent = []
            for x in range(x1, x2 + stride_1, stride_1):
                for y in range(y1, y2 + stride_2, stride_2):
                    point = (x, y)
                    vent.append(point)

            # append the vent to the vents
            vents.append(vent)

    return highest_x, highest_y, vents


def highest(highest_x, highest_y, x1, x2, y1, y2):
    # yes, i am open for suggestions

    if x1 > highest_x:
        highest_x = x1

    if x2 > highest_x:
        highest_x = x2

    if y1 > highest_y:
        highest_y = y1

    if y2 > highest_y:
        highest_y = y2

    return highest_x, highest_y


if __name__ == '__main__':
    main()
