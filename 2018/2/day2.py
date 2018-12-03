from collections import Counter

with open('input.txt') as f:
    twos, threes = 0, 0
    for line in f.readlines():
        lc = Counter(line)
        vals_set = set(x for x in lc.values() if x != 1)
        if 2 in vals_set:
            twos += 1
        if 3 in vals_set:
            threes += 1
    print(twos*threes)

