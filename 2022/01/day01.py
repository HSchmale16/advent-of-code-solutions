import sys

sums = []
s = 0
for line in sys.stdin.readlines():
    if line == '\n':
        sums.append(s)
        s = 0
    else:
        s += int(line)

print(max(sums))
