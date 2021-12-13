FILE = "example"


def main():
    dots, folds = parse_input()
    print(dots)
    print(folds)


def parse_input():
    dots = []
    folds = []
    with open(FILE) as lines:
        for line_raw in lines:
            line = line_raw.strip()

            if len(line) == 0:
                continue

            if line.startswith("fold along "):
                folds.append(line[11:])
                continue

            x, y = line.split(",")
            dots.append((int(x), int(y)))

    return dots, folds


if __name__ == '__main__':
    print(main())
