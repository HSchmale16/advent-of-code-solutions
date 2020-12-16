import sys 
from math import sin, cos, pi

x, y = 0, 0
direction = 0

for line in sys.stdin.readlines():
    cmd, distance = line[0], int(line[1:])
    if cmd == 'N':
        y += distance
    elif cmd == 'S':
        y -= distance
    elif cmd == 'E':
        x += distance
    elif cmd == 'W':
        x -= distance
    elif cmd == 'L':
        direction += distance
    elif cmd == 'R':
        direction -= distance
    elif cmd == 'F':
        radians = (direction / 180) * pi
        x += cos(radians) * distance
        y += sin(radians) * distance

print("Part 1", abs(x) + abs(y))
