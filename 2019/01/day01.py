#!/usr/bin/env python3

import sys
import math

def fuel(x):
    return math.trunc(x / 3) - 2

counter1 = 0
counter2 = 0
for line in sys.stdin.readlines():
    x = int(line)
    fuel1 = fuel(x)
    counter1 += fuel1
    fuel2 = fuel1
    while fuel1 > 0:
        fuel1 = fuel(fuel1)
        fuel2 += fuel1 if fuel1 > 0 else 0
    counter2 += fuel2

print(counter1)
print(counter2)
