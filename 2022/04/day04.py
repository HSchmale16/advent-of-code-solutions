import sys

part1 = 0
part2 = 0
for line in sys.stdin.readlines():
    a, b = line.split(',')
    a1, a2 = map(int, a.split('-'))
    b1, b2 = map(int, b.split('-'))

    if b1 >= a1 and b2 <= a2:
        part1 += 1
    elif a1 >= b1 and a2 <= b2:
        part1 += 1

    s1 = set(range(a1, a2+1))
    s2 = set(range(b1, b2+1))
    if len(s1.intersection(s2)) > 0:
        part2 += 1


print(part1)
print(part2)
