import sys
from collections import Counter
from collections import deque

def try_int(x):
    try:
        return int(x.replace(',', ''))
    except ValueError:
        return x.replace(',', '')

with open(sys.argv[1]) as f:
    CMDS = [tuple(map(try_int, line.split())) for line in f.readlines()]

class DuetRunner:
    def __init__(self, r, s, p):
        assert r is not s
        self.progcnter = 0
        self.r_queue = r
        self.s_queue = s
        self.regs = Counter({'p': p})
        self.waiting = False
        self.snd_count = 0
    
    def get_value(self, target):
        if type(target) is int:
            return target
        return self.regs[target]

    def run(self):
        cmd = CMDS[self.progcnter]
        ins = cmd[0]
        if ins == 'snd':
            self.s_queue.append(self.get_value(cmd[1]))
            self.snd_count += 1
        elif ins == 'set':
            self.regs[cmd[1]] = self.get_value(cmd[2])
        elif ins == 'add':
            self.regs[cmd[1]] += self.get_value(cmd[2])
        elif ins == 'mul':
            self.regs[cmd[1]] *= self.get_value(cmd[2])
        elif ins == 'mod':
            self.regs[cmd[1]] %= self.get_value(cmd[2])
        elif ins == 'rcv':
            if len(self.r_queue) == 0:
                self.waiting = True
                return
            else:
                self.waiting = False
                self.regs[cmd[1]] = self.r_queue.popleft()
        elif ins == 'jgz':
            if self.get_value(cmd[1]) > 0:
                self.progcnter += self.get_value(cmd[2])
                return
        self.progcnter += 1

prog0_q = deque()
prog1_q = deque()

prog0 = DuetRunner(prog0_q, prog1_q, 0)
prog1 = DuetRunner(prog1_q, prog0_q, 1)

while True:
    #print(len(prog0_q), len(prog1_q))
    prog0.run()
    prog1.run()
    if prog0.waiting and prog1.waiting:
        break

print(prog0.snd_count)
print(prog1.snd_count)
