import sys

dx, dy = (0, 0) 
houses = {(0,0)}
with open(sys.argv[1]) as f:
    for c in f.read():
        if   c == '^': dy += 1
        elif c == 'v': dy -= 1
        elif c == '<': dx -= 1
        elif c == '>': dx += 1

        houses.add((dx, dy))

print(len(houses))
