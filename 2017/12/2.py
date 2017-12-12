import sys
import networkx

g = networkx.Graph()
with open(sys.argv[1]) as f:
    for line in f:
        l = line.replace(',', '').split()
        del l[1]
        l = [int(x) for x in l]
        for v in l[1:]:
            g.add_edge(l[0], v)
    print(networkx.number_connected_components(g))
