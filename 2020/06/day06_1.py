import sys

groups = []
cur_group = set()
for line in sys.stdin.readlines():
    line = line.strip()
    if line == "":
        groups.append(cur_group)
        cur_group = set()
        continue
    for c in line:
        cur_group.add(c)
groups.append(cur_group)
print(sum((len(s) for s in groups)))
