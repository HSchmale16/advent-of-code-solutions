import sys
from collections import namedtuple


Node = namedtuple("Node", ['name', 'weight', 'childs']) 
nodes = {} 

def parse_line(line):
    fields = line.split()
    weight = fields[1][1:-1]
    childs = []
    if len(fields) > 3:
        childs = list(map(lambda x: x.replace(',', ''), fields[3:])) 
    return Node(fields[0], weight, childs) 

def squash_set_remove(s, key):
    try:
        s.remove(key)
    except KeyError:
        print('Fuck') 

with open(sys.argv[1]) as f:
    for line in f.readlines():
        n = parse_line(line)
        print(n)
        nodes[n.name] = n

unmentioned_nodes = set(nodes.keys())
for key,node in nodes.items():
    if len(node.childs) > 0:
        [squash_set_remove(unmentioned_nodes, n) for n in node.childs]
    else:
        squash_set_remove(unmentioned_nodes, key)
   
print(unmentioned_nodes)
