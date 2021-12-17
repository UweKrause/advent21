FILE = "example"


def main():
    template, rules = parse_input()
    print("t:", template)
    print("r:", rules)


def parse_input():
    """parse input to numbers drawn and boards available"""

    with open(FILE) as lines:
        # first line contains the template
        template = lines.readline().strip()

        # second line is empty
        _ = lines.readline()

        # extract all the rules from remaining input
        rules = {}
        for line in lines.readlines():
            rule_replace, rule_replace_with = line.strip().split(" -> ")
            rules[rule_replace] = rule_replace_with

    return template, rules


if __name__ == '__main__':
    print(main())
