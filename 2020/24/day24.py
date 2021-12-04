import sys

black_tiles = set()
for line in map(str.strip, sys.stdin.readlines()):
    i = 0
    x, y = 0, 0
    while i < len(line):
        if line[i] in ('n', 's'):
            if line[i] == 'n':
                y += 1
            else:
                y -= 1
            if line[i+1] == 'e':
                x += 1
            else:
                x -= 1
            i += 2
        else:
            if line[i] == 'e':
                x += 2
            elif line[i] == 'w':
                x -= 2
            i += 1
    if (x,y) in black_tiles:
        black_tiles.remove((x,y))
    else:
        black_tiles.add((x,y))
print("part 1", len(black_tiles))

def btba(axis):
    return [b[axis] for b in black_tiles]

def adj(x,y):
    yield (x+1,y)
    yield (x, y+1)
    yield (x-1, y+1)
    yield (x-1,y)
    yield (x-1, y-1)
    yield (x, y-1)

print(list(adj(3,2)))

for i in range(100):
    next_bt = set()
    x_min, x_max = min(btba(0)), max(btba(0))
    y_min, y_max = min(btba(1)), max(btba(1))

    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            count = 0
            for a in adj(x,y):
                if a in black_tiles:
                    count += 1
            if (x,y) in black_tiles:
                if not (count == 0 or count >= 2):
                    next_bt.add((x,y))
            else:
                if count == 2:
                    next_bt.add((x,y))
    print("part 2", i, len(black_tiles))
    black_tiles = next_bt


