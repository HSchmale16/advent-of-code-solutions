import sys

sums = []
s = 0
for line in sys.stdin.readlines():
    if line == '\n':
        sums.append(s)
        s = 0
    else:
        s += int(line)
sums.append(s)

sums.sort()
sums.reverse()
print(sum(sums[:3]))
