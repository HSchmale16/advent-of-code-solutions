import sys

def calc_score(c):
    if c.isupper():
        return ord(c) - ord('A') + 27
    return ord(c) - ord('a') + 1

score = 0
lines = [l for l in map(str.strip, sys.stdin.readlines())]
for i in range(0, len(lines), 3):
    l1 = set(lines[i])
    l2 = l1.intersection(set(lines[i+1]))
    l3 = l2.intersection(set(lines[i+2]))

    x = list(l3)[0]
    score += calc_score(x)

print(score)

