import sys
from collections import namedtuple


Node = namedtuple("Node", ['name', 'weight', 'childs']) 
nodes = {} 

def parse_line(line):
    fields = line.split()
    weight = int(fields[1][1:-1])
    childs = []
    if len(fields) > 3:
        childs = list(map(lambda x: x.replace(',', ''), fields[3:])) 
    return Node(fields[0], weight, childs) 

def squash_set_remove(s, key):
    try:
        s.remove(key)
    except KeyError:
        pass

def build_tree(key):
    node = nodes[key]
    childs = []
    if len(node.childs) != 0:
        childs = list(map(build_tree, node.childs))
    return Node(node.name, node.weight, childs)

def find_root(nodes):
    unmentioned_nodes = set(nodes.keys())
    for key,node in nodes.items():
        if len(node.childs) > 0:
            [squash_set_remove(unmentioned_nodes, n) for n in node.childs]
        else:
            squash_set_remove(unmentioned_nodes, key)
    return list(unmentioned_nodes)[0]


def sum_tree(root):
    if len(root.childs) == 0:
        return root.weight
    return root.weight + sum(map(sum_tree, root.childs))

def check_equal(iterator):
    return len(set(iterator)) <= 1

def find_unbalance(root, delta=None):
    values = [sum_tree(n) for n in root.childs]
    if delta is None:
        delta = max(values) - min(values)
    print(values)
    if check_equal(values):
        print(root.weight - delta)
    else:
        find_unbalance(root.childs[values.index(max(values))], delta)


with open(sys.argv[1]) as f:
    for line in f.readlines():
        n = parse_line(line)
        nodes[n.name] = n


root = build_tree(find_root(nodes))
print(find_unbalance(root)) 


