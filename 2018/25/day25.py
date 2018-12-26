import sys
import networkx as nx
import matplotlib.pyplot as plt

def manhatten(a, b):
    return sum(abs(x - y) for x,y in zip(a,b))

if __name__ == '__main__':
    data = [[int(x) for x in line.split(',')] for line in
            open(sys.argv[1]).readlines()]

    g = nx.Graph()

    for i,star1 in enumerate(data):
        g.add_node(i)
        for j,star2 in enumerate(data):
            if i != j and manhatten(star1, star2) <= 3:
                g.add_edge(i, j)

    print(nx.number_connected_components(g))
