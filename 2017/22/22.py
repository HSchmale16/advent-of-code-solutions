import sys
import math
import operator

def clamp_dir(dr, incre):
    dr += incre
    if dr < 0:
        return 3
    elif dr > 3:
        return 0
    return dr

dirs = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0)
]
current = 0
x, y = (0,0)

grid = {}
with open(sys.argv[1]) as f:
    for row, line in enumerate(f.readlines()):
        line = line.strip()
        x = int(math.floor(len(line) / 2))
        y += 1
        for col, char in enumerate(line):
            grid[col,row] = True if char == '#' else False
    y = int(math.floor(y / 2))
print(x,y)

cleaned, infected = 0, 0
for i in range(10000):
    try:
        pos = grid[x,y]
    except KeyError:
        pos = False

    if pos:
        print('right')
        current = clamp_dir(current, 1)
        grid[x,y] = False
        cleaned += 1
    else:
        print('left')
        current = clamp_dir(current, -1)
        grid[x,y] = True
        infected += 1
    x, y = map(operator.add, (x,y), dirs[current])
    print(x,y)

print(cleaned, infected)
