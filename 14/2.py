from collections import defaultdict

FILE = "input"

STEPS = 40

"""
Code for Part 2 is exactly the same as for 1.
"""


def main():
    template, rules = parse_input()

    pairs, letters = extract_pairs_and_letters(template)

    _, letters = get_segments(pairs, letters, rules)

    return max(letters.values()) - min(letters.values())


def extract_pairs_and_letters(template):
    pairs = defaultdict(int)
    letters = defaultdict(int)
    for i in range(len(template) - 1):
        pairs[template[i] + template[i + 1]] += 1
        letters[template[i]] += 1
    # don't forget the last letter
    letters[template[-1]] += 1
    return pairs, letters


def get_segments(pairs, letters, rules):
    for step in range(1, STEPS + 1):

        pairs_before = defaultdict(int, pairs.copy())
        pairs_after = defaultdict(int, pairs.copy())

        for pair, pair_count in pairs_before.items():

            for rule_replace, rule_replacement in rules.items():

                if pair != rule_replace:
                    continue

                replacement1 = pair[0] + rule_replacement
                replacement2 = rule_replacement + pair[1]

                # change pairs
                pairs_after[pair] -= pair_count
                pairs_after[replacement1] += pair_count
                pairs_after[replacement2] += pair_count

                # append letter
                letters[rule_replacement] += pair_count

        # get rid of pairs with zero or negative occurrence
        pairs = {x: y for x, y in pairs_after.items() if y > 0}

        if FILE == "example":
            check_example(pairs, letters, step)

    return pairs, letters


def check_example(pairs, letters, step):
    check = {
        0: "NNCB",
        1: "NCNBCHB",
        2: "NBCCNBBBCBHCB",
        3: "NBBBCNCCNBBNBNBBCHBHHBCHB",
        4: "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB",
    }

    if step in check.keys():
        pairs1, letters1 = extract_pairs_and_letters(check[step])
        assert pairs == pairs1
        assert letters == letters1


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
            rule_insert_where, rule_insert_what = line.strip().split(" -> ")

            if len(rule_insert_where) != 2 or len(rule_insert_what) != 1:
                raise NotImplementedError

            rules[rule_insert_where] = rule_insert_what

    return template, rules


if __name__ == '__main__':
    print(main())  # 3447389044530
