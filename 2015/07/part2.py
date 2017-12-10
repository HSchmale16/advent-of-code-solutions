# 2015 Day 7

import sys
import ctypes 
import networkx
import re

GATES = {
    'AND':      lambda x, y: x.value & y.value,
    'OR':       lambda x, y: x.value | y.value,
    'LSHIFT':   lambda x, y: x.value << y.value,
    'RSHIFT':   lambda x, y: x.value >> y.value,
    'NOT':      lambda x, y: ~ x.value,
    '->':       lambda x, y: x.value
}

def tryint(x):
    try:    return ctypes.c_uint16(int(x))
    except: 
        return x

class Instruct:
    def __init__(self, tpl):
        self.result = tpl[-1]
        if len(tpl) in [3, 5]:
            self.op0 = tpl[0]
            self.op1 = tpl[2] if len(tpl) == 5 else None
            self.cmd = GATES[tpl[1]]
        else:
            self.op0 = tpl[1]
            self.op1 = None
            self.cmd = GATES[tpl[0]]
        self.wires = []
        for x in tpl[:-1]:
            if type(x) is str and x.isalpha() and x.islower():
                self.wires.append(x) 

    def run(self, r):
        return self.cmd(self._op0(r), self._op1(r))
    
    def _op(self, r, v):
        if type(v) is ctypes.c_uint16:  return v
        elif v is None:                 return 0
        else:                           return r[v]

    def _op0(self, r):
        return self._op(r, self.op0)
        
    def _op1(self, r):
        return self._op(r, self.op1)

def calc_regs(regs, graph, instructs):
    for wire in reversed(list(networkx.topological_sort(graph))):
        regs[wire] = ctypes.c_uint16(instructs[wire].run(regs))

def main():
    instructs = {}
    regs = {}
    graph = networkx.DiGraph()
    with open(sys.argv[1]) as f:
        for line in f.readlines():
            cmd = tuple(tryint(i) for i in line.split())
            i = Instruct(cmd)
            graph.add_node(i.result)
            for x in i.wires:
                graph.add_node(x)
                graph.add_edge(i.result, x)
            instructs[i.result] = i

    calc_regs(regs, graph, instructs)
    instructs['b'] = Instruct((regs['a'], '->', 'b'))
    regs = {}
    calc_regs(regs, graph, instructs)

    for k, v in regs.items():
        print(k, v.value)
if __name__ == '__main__':
    main()
