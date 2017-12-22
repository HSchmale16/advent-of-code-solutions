import sys
import math
import operator
from collections import defaultdict

def clamp_dir(dr, incre):
    return (dr + incre) % 4

CLEAN = 0
WEAKENED = 1
INFECTED = 2
FLAGGED = 3

dirs = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0)
]
current = 0
x, y = (0,0)

grid = defaultdict(lambda: CLEAN)
with open(sys.argv[1]) as f:
    for row, line in enumerate(f.readlines()):
        line = line.strip()
        x = int(math.floor(len(line) / 2))
        y += 1
        for col, char in enumerate(line):
            grid[col,row] = INFECTED if char == '#' else CLEAN
    y = int(math.floor(y / 2))
print(x,y)


infected = 0
for i in range(10000000):
    pos = grid[x,y]

    if pos == CLEAN:
        current = clamp_dir(current, -1)
    elif pos == WEAKENED:
        infected += 1
    elif pos == INFECTED:
        current = clamp_dir(current, 1)
    else:
        current = clamp_dir(current, 2)

    grid[x,y] = clamp_dir(pos, 1)

    x, y = map(operator.add, (x,y), dirs[current])

print(infected)
