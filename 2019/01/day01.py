import sys
import math

counter1 = 0
counter2 = 0
for line in sys.stdin.readlines():
    x = int(line)
    fuel1 = math.trunc(x / 3) - 2
    counter1 += fuel1
    fuel2 = fuel1
    while fuel1 > 0:
        fuel1 = math.trunc(fuel1 / 3) - 2
        if fuel1 > 0:
            fuel2 += fuel1
    counter2 += fuel2

print(counter1)
print(counter2)
