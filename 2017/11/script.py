import sys
import operator

DIR_MAP = {
    'nw': (-1, 1, 0),
    'se': (1, -1, 0),
    'n' : ( 0,  1, -1),
    's' : ( 0, -1, 1),
    'ne': ( 1, 0, -1),
    'sw': (-1, 0, 1)
}

def move_dir(dr, current):
    return tuple(map(operator.add, current, DIR_MAP[dr]))

def distance(pos):
    return sum(map(abs, pos)) / 2.0


with open(sys.argv[1]) as f:
    cur = (0, 0, 0)
    max_dis = 0
    for d in f.read().strip().split(','):
        if d in DIR_MAP:
            cur = move_dir(d, cur)
        max_dis = distance(cur) if distance(cur) > max_dis else max_dis

print(max_dis)
