from collections import defaultdict
from itertools import permutations

vertex = set()
edges = defaultdict(lambda: {})
with open('input') as f:
    for line in f.readlines():
        fields = line.split()
        value = lambda: {"weight": int(fields[-1])}
        edges[fields[0]].update({fields[2]: value()})
        edges[fields[2]].update({fields[0]: value()})
        vertex.add(fields[0])
        vertex.add(fields[2])        

def weight(u, v): return edges[u][v]["weight"]

# Use a big number
min_cost = 10**50
vtxs = list(vertex)

for perm in permutations(vtxs):
    cost = 0
    for i in range(1, len(perm)):
        cost += weight(perm[i - 1], perm[i])
    if cost < min_cost:
        min_cost = cost

print(min_cost) 
