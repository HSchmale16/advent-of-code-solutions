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

ordering = nx.lexicographical_topological_sort(g)
# Part 1 done

# Part 2



