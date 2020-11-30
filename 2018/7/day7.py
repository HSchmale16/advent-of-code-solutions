import networkx as nx

# Part 1
g = nx.DiGraph()
while True:
    try:
        x = input()
        edges = [y for y in x.split() if len(y) == 1]
        g.add_edge(*edges)
    except EOFError:
        break

ordering = list(nx.lexicographical_topological_sort(g))
print (*ordering)
# Part 1 done

# Part 2
STEP_INCR = 60


class Worker:
    def __init__(self, step):
        self.time_remaining = ord(step) - ord('A') + STEP_INCR
        self.step = step



done_steps = set()
timestep = 0



