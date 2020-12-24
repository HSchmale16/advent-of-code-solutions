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
print(len(black_tiles))
