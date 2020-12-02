from itertools import combinations

with open('input.txt') as f:
    l = [int(x) for x in f.readlines()]

for (a,b,c) in combinations(l, 3):
    if a + b + c == 2020:
        print(a*b*c)
        break
for (a,b) in combinations(l, 2):
    if a + b == 2020:
        print(a*b)
        break
