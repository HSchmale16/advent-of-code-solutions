import sys 
from math import sin, cos, pi, sqrt, atan2

ship_x, ship_y = 0, 0
wx, wy = 10,1


def compute_rotation(degrees):
    radians = degrees * (pi / 180)
    
    rotation = atan2(wx, wy)
    rotation += radians

    v_dis = sqrt(wx ** 2 + wy ** 2)

    new_x = sin(rotation) * v_dis
    new_y = cos(rotation) * v_dis

    return new_x, new_y


for line in sys.stdin.readlines():
    cmd, distance = line[0], int(line[1:])
    if cmd == 'N':
        wy += distance
    elif cmd == 'S':
        wy -= distance
    elif cmd == 'E':
        wx += distance
    elif cmd == 'W':
        wx -= distance
    elif cmd == 'L':
        wx, wy = compute_rotation(-distance)
    elif cmd == 'R':
        wx, wy = compute_rotation(distance)
    elif cmd == 'F':
        rotation = atan2(wx, wy)
        ship_x += wx * distance
        ship_y += wy * distance


    print(cmd, distance, ship_x, ship_y, wx, wy)

print("Part 2", abs(ship_x) + abs(ship_y))
