import sys
from typing import Tuple

class MinMax:
    __slots__ = ['low', 'high']

    def __init__(self):
        self.low = 0
        self.high = 0
    
    def add(self, val):
        self.low = min(self.low, val)
        self.high = max(self.high, val)

    def mk_range(self):
        return range(self.low - 1, self.high + 3)


class PointsBox:
    __slots__ = ['points', 'minmax']

    def __init__(self):
        self.points = set()
        self.minmax = [MinMax(), MinMax(), MinMax(), MinMax()]

    def add(self, p):
        self.points.add(p)
        for mm, x in zip(self.minmax, p):
            mm.add(x)

    def generate_points(self):
        for x in self.minmax[0].mk_range():
            for y in self.minmax[1].mk_range():
                for z in self.minmax[2].mk_range():
                    for w in self.minmax[3].mk_range():
                        yield x,y,z,w

    def __contains__(self, item):
        return self.points.__contains__(item)


def points_around(x0, y0, z0, w0): 
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            for z in [-1, 0, 1]:
                for w in [-1, 0, 1]:
                    if (x,y,z,w) != (0,0,0,0):
                        yield (x0 + x, y0 + y, z0 + z, w0 + w)

def count_active(point, pbox : PointsBox):
    count = 0
    for p in points_around(*point):
        if p in pbox.points:
            count += 1
    return count

def to_be_active(point : Tuple[int,int,int,int], pbox : PointsBox):
    count = count_active(point, pbox)
        #if count >= 4:
        #    return False # Nothing happens if more than 3 are lit
    # is active
    if point in pbox.points:
        return count == 2 or count == 3
    # otherwise only turn on w/ exactly 3 neighbors
    return count == 3


    


points = PointsBox()
for y, line in enumerate(map(str.strip, sys.stdin.readlines())):
    for x, c in enumerate(line):
        if c == '#':
            points.add((x, y, 0, 0))


for i in range(6):
    next_iter = PointsBox()
    for p in points.generate_points():
        if to_be_active(p, points):
            next_iter.add(p)
    points = next_iter

print(len(points.points))

