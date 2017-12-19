import sys
from collections import Counter


def try_int(x):
    try: return int(x.replace(',', ''))
    except: return x.replace(',', '')

regs = Counter()
cmds = []

with open(sys.argv[1]) as f:
    cmds = [tuple(map(try_int, line.split())) for line in f.readlines()]
print(cmds)
progcnter = 0

def get_value(target):
    if type(target) is int:
        return target
    return regs[target]

try:
    last = None
    while True:
        print(regs, progcnter)
        cmd = cmds[progcnter]
        ins = cmd[0]
        if ins == 'snd':
            last = get_value(cmd[1])
            print(last)
        elif ins == 'set':
            regs[cmd[1]] = get_value(cmd[2])
        elif ins == 'add':
            regs[cmd[1]] += get_value(cmd[2])
        elif ins == 'mul':
            regs[cmd[1]] *= get_value(cmd[2])
        elif ins == 'mod':
            regs[cmd[1]] %= get_value(cmd[2])
        elif ins == 'rcv':
            if get_value(cmd[1]) != 0:
                print(last)
                break
        elif ins == 'jgz':
            if get_value(cmd[1]) > 0:
                progcnter += get_value(cmd[2])
                continue
        progcnter += 1
except:
    print(regs)
