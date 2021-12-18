from collections import defaultdict

FILE = "input"
STEPS = 10


def main(steps):
    template, rules = parse_input()

    pairs, letters = extract_pairs_and_letters(template)

    letters = get_lettercounts(pairs, letters, rules, steps)

    return max(letters.values()) - min(letters.values())


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


def extract_pairs_and_letters(template):
    pairs = defaultdict(int)
    letters = defaultdict(int)

    for i in range(len(template) - 1):
        pair = template[i] + template[i + 1]
        pairs[pair] += 1
        letters[template[i]] += 1

    # don't forget the last letter
    letters[template[-1]] += 1

    return pairs, letters


def get_lettercounts(pairs, letters, rules, steps):
    for step in range(1, steps + 1):

        pairs_working_copy = defaultdict(int, pairs)

        for pair, pair_count in pairs.items():

            for rule_replace, rule_replacement in rules.items():

                if pair != rule_replace:
                    continue

                pair_new_left = pair[0] + rule_replacement
                pair_new_rigth = rule_replacement + pair[-1]

                # adjust pair count in working copy
                pairs_working_copy[pair] -= pair_count
                pairs_working_copy[pair_new_left] += pair_count
                pairs_working_copy[pair_new_rigth] += pair_count

                # append letter
                letters[rule_replacement] += pair_count

        pairs = pairs_working_copy

    return letters


if __name__ == '__main__':
    print(main(STEPS))  # 3058
