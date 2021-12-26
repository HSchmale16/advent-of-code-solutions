from sys import stdin
from functools import reduce
import operator
import numpy as np

lines = [l.strip() for l in stdin.readlines()]
size1,size2 = (len(lines)), (len(lines[0]))
print(size1, size2)

octopi = np.full([size1, size2], 0)

def step(octopi_in):
    octopi = octopi_in.copy()
    flashed = np.full([size1, size2], 0)
    flash_count = 0
    
    octopi += 1

    iter_flash = True

    while iter_flash:
        iter_flash = False
        for y in range(size1):
            for x in range(size2):
                if octopi[y,x] > 9 and not flashed[y,x]:
                    flashed[y,x] = 1
                    iter_flash = True
                    for i in [-1, 0, 1]:
                        for j in [-1, 0, 1]:
                            if (0 <= y + i < size1) and (0 <= x + j < size2):
                                octopi[y+i,x+j] += 1
                    octopi[y,x] -= 1

    for y in range(10):
        for x in range(10):
            if flashed[y,x]:
                octopi[y,x] = 0

    return flashed.sum(), octopi

for y, line in enumerate(lines):
    for x, c in enumerate(line):
        octopi[y,x] = int(c)

print(octopi)

total_flash = 0
i = 1
while True:
    flash, octopi = step(octopi)
    total_flash += flash

    if i in (20, 100):
        print(f'Part 1: {i=} {total_flash=}')

    if flash == 100:
        print(f'Part 2: {i=}')
        break

    i += 1





