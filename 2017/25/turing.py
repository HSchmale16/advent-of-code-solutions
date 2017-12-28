from collections import deque
import networkx as nx
import sys

def get_state(line):
    return line.split()[-1][0]

def try_int(x):
    try:
        return int(x)
    except ValueError:
        return x

def load_state_trans(f):
    def edge_add(g, u, d):
        d = [try_int(x) for x in d]
        g.add_edge(u, d[-1], data=d) 
    g = nx.MultiDiGraph()
    current_node = None
    edge_details = []
    for line in f.readlines():
        line = line.strip()
        if line.startswith("In"):
            if current_node is not None:
                edge_add(g, current_node, edge_details)
                edge_details = []
            current_node = get_state(line)
        elif line.startswith('If'):
            if edge_details:
                edge_add(g, current_node, edge_details)
            edge_details = [get_state(line)]
        elif not line:
            continue
        else:
            edge_details.append(get_state(line))
    edge_add(g, current_node, edge_details)
    return g

def move(tape, position, d):
    if d == 'l':
        if position == 0:
            tape.appendleft(0)
            return 0
        return position - 1
    elif d == 'r':
        if position + 1 == len(tape):
            tape.append(0)
            return position + 1
        return position + 1 

def step(g, tape, state, position):
    cur_value = tape[position]
    for u, v, d in g.out_edges(state, data=True):
        if d['data'][0] == cur_value:
            tape[position] = d['data'][1]
            position = move(tape, position, d['data'][-2])
            state = v
            return state, position 
    raise ValueError("Couldn't find state transition for current")

def main(): 
    f = open(sys.argv[1])

    state = f.readline().split()[-1][:-1]
    steps = int(f.readline().split()[-2])

    g = load_state_trans(f)    
    tape = deque([0])
    position = 0 

    for i in range(steps):
        state, position = step(g, tape, state, position)
    
    print(tape.count(1))

if __name__ == '__main__':
    main()
