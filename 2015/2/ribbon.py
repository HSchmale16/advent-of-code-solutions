import sys

def area(l, w, h):
    side_areas = [l*w, w*h, h*l]
    min_side = min(side_areas)
    return sum(map(lambda x: 2*x, side_areas)) + min_side

def rib(l, w, h):
    perims = [2*l + 2*w, 2*w + 2*h, 2*h + 2*l]
    return min(perims) + (l*w*h)

ribl = [rib(*map(int, line.split('x'))) for line in sys.stdin.readlines()]
print(sum(ribl))

