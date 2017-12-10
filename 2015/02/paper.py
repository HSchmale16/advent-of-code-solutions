import sys

def area(l, w, h):
    side_areas = [l*w, w*h, h*l]
    min_side = min(side_areas)
    return sum(map(lambda x: 2*x, side_areas)) + min_side

areas = [area(*map(int, line.split('x'))) for line in sys.stdin.readlines()]
print(sum(areas))

