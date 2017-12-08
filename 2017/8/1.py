import sys
from collections import Counter

class Cmd:
    def __init__(self, tup):
        self.reg = tup[0]
        self.value = int(tup[2])
        if tup[1] == 'dec': self.value *= -1
        self.test_reg = tup[4]
        self.check = tup[5]
        self.test_val = int(tup[6]) 

    def go(self, regs):
        test = regs[self.test_reg]
        if eval("test {} {}".format(self.check, self.test_val)):
            regs[self.reg] += self.value


regs = Counter()
abs_max = 0
with open(sys.argv[1]) as f:
    for line in f.readlines():
        Cmd(line.split()).go(regs)
        if len(regs) and max(regs.values()) > abs_max:
            abs_max = max(regs.values())
print(abs_max)
