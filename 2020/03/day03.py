import sys
from functools import reduce
from operator import mul


grid = [line.strip() for line in sys.stdin.readlines()]

def slope(vx, vy):
    y = 1
    x = 0
    trees = 0
    for line in grid[::vy]:
        if line[x%len(line)] == '#':
            trees += 1 
        x += vx
        y += vy
    return trees

# Part 1
print(slope(3, 1))

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
print(reduce(mul, [slope(*s) for s in slopes]))
