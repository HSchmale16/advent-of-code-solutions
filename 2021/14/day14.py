from sys import stdin
from collections import Counter


def apply_rules(initial, rules : dict):
    new_str = ""
    for i in range(len(initial) - 1):
        my_pair = initial[i:i+2]
        new_str += my_pair[0]
        option = rules.get(my_pair, None)
        if option is not None:
            new_str += option
    new_str += my_pair[1]

    return new_str


def apply_rules_count_pairs(intital : Counter, freq: Counter, rules : dict):    
    cnt = Counter()
    for k,v in intital.items():
        if k in rules:
            c = rules[k]
            a = k[0] + c
            b = c + k[1]
            cnt[a] += v
            cnt[b] += v
            freq[c] += v
        else:
            cnt[k] += v
    return cnt, freq


def from_pair_to_letter_freq(c : Counter):
    c2 = Counter()
    for k,v in c.items():
        c2[k[0]] += v
        c2[k[1]] += v
    return c2


def get_input():
    initial = input()

    # skip
    input()
    rules = {}
    for line in stdin.readlines():
        pair, arrow, to = line.split()
        rules[pair] = to

    return initial, rules


def most_least_diff(new):
    if type(new) is not Counter:
        c = Counter(new)
    else:
        c = new
    mc = c.most_common()
    most, least = mc[0], mc[-1]
    return most[1] - least[1]


def part1():
    initial, rules = get_input()
    new = apply_rules(initial, rules)
    for i in range(9):
        new = apply_rules(new, rules)

    print("Part 1: ", most_least_diff(new))

def main():
    initial, rules = get_input()

    pairs = Counter()
    freq = Counter(initial)

    for i in range(len(initial) - 1):
        my_pair = initial[i:i+2]
        pairs[my_pair] += 1

    print(pairs, freq)

    for i in range(40):
        if i == 9:
            print("Part 1: ", most_least_diff(freq))

        pairs, freq = apply_rules_count_pairs(pairs, freq, rules)


    print("Part 2: ", most_least_diff(freq))


if __name__ == '__main__':
    main()