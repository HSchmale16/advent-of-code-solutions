import sys
from collections import Counter

lines = []
for line in sys.stdin.readlines():
    l = line.replace(",", " ")
    fields = l.split()
    x0, y0, _, x1, y1 = fields
    lines.append([int(v) for v in (x0, y0, x1, y1)])

filled_spaces = Counter()
for x0,y0,x1,y1 in lines:
    if x0 == x1:
        for y in range(min(y0, y1), max(y0, y1) + 1):
            filled_spaces[(x0, y)] += 1
    elif y0 == y1:
        for x in range(min(x0, x1), max(x0, x1) + 1):
            filled_spaces[(x,y0)] += 1

print(sum(1 for v in filled_spaces.values() if v > 1))

# Begin part 2

filled_spaces = Counter()
for x0,y0,x1,y1 in lines:
    if x0 == x1:
        for y in range(min(y0, y1), max(y0, y1) + 1):
            filled_spaces[(x0, y)] += 1
    elif y0 == y1:
        for x in range(min(x0, x1), max(x0, x1) + 1):
            filled_spaces[(x,y0)] += 1
    else:
        distance = max(x0, x1) - min(x0, x1) + 1
        if x0 < x1:
            if y0 < y1:
                for i in range(distance):
                    filled_spaces[(x0 + i, y0 + i)] += 1
            else:
                for i in range(distance):
                    filled_spaces[(x0 + i, y0 - i)] += 1
        else:
            if y0 < y1:
                for i in range(distance):
                    filled_spaces[(x0 - i, y0 + i)] += 1
            else:
                for i in range(distance):
                    filled_spaces[(x0 - i, y0 - i)] += 1
                
print(sum(1 for v in filled_spaces.values() if v > 1))
