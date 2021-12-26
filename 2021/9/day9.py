from sys import stdin
from functools import reduce
import operator
import numpy as np

lines = [l.strip() for l in stdin.readlines()]
size1,size2 = (len(lines) + 2), (len(lines[0]) + 2)
print(size1, size2)

heights = np.full([size1, size2], 10)

def bfs_size(start_pos, heights):
    def queue_add(pos, queue, explored):
        if heights[pos[0], pos[1]] == 9:
            return queue
        if pos in queue or pos in explored:
            return queue
        queue.append(pos)
        return queue

    queue = [start_pos]
    explored = set()
    while len(queue) != 0:
        y,x = queue.pop(0)
        h = heights[y,x]
        if y >= 1 and (y+2 < size1) and heights[y+1,x] > h:
            queue = queue_add((y+1,x), queue, explored)
        if y >= 2 and y < size1 and heights[y-1,x] > h: 
            queue = queue_add((y-1,x), queue, explored)
        if x >= 1 and (x+2 < size2) and heights[y,x+1] > h:
            queue = queue_add((y,x+1), queue, explored)
        if x >= 2 and x < size2 and heights[y,x-1] > h:
            queue = queue_add((y,x-1), queue, explored)

        explored.add((y,x))

    print(explored)
    return len(explored)


for y, line in enumerate(lines, start=1):
    for x, c in enumerate(line, start=1):
        heights[y,x] = int(c)

print(heights)


risk_level = 0
low_points = []
basin_sizes = []
for y in range(1, size1):
    for x in range(1, size2):
        t = heights[y,x]
        if t < heights[y-1,x] and t < heights[y+1,x] and \
                t < heights[y,x+1] and t < heights[y,x-1]:
            risk_level += t + 1
            low_points.append((y,x))
            basin_sizes.append(bfs_size((y,x), heights))

print(risk_level)
print(low_points)
print(basin_sizes)

basin_sizes.sort()

top3 = basin_sizes[len(basin_sizes) - 3:]
product = reduce(operator.mul, top3, 1)
print(product)





