import sys
from collections import Counter

groups = []
cur_group = Counter()
people = 0
for line in sys.stdin.readlines():
    line = line.strip()
    if line == "":
        groups.append({k:v for k,v in cur_group.items() if v == people})
        cur_group = Counter()
        people = 0
        continue
    
    people += 1
    for c in line:
        cur_group[c] += 1

groups.append({k:v for k,v in cur_group.items() if v == people})
print(sum((len(s) for s in groups)))
