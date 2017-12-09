from collections import Counter


def try_int(x):
    try: return int(x.replace(',', ''))
    except: return x.replace(',', '')

regs = Counter({'a': 1})
cmds = []

with open('input') as f:
    cmds = [tuple(map(try_int, line.split())) for line in f.readlines()]
print(cmds)
progcnter = 0

try:
    while True:
        print(regs, progcnter)
        cmd = cmds[progcnter]
        ins = cmd[0]
        if ins == 'hlf':
            regs[cmd[1]] /= 2
        elif ins == 'tpl':
            regs[cmd[1]] *= 3
        elif ins == 'inc':
            regs[cmd[1]] += 1
        elif ins == 'jmp':
            progcnter += cmd[1]
            continue
        elif ins.endswith('e') and regs[cmd[1]] % 2 == 0:
            progcnter += cmd[2]
            continue
        elif ins.endswith('o') and regs[cmd[1]] == 1:
            progcnter += cmd[2]
            continue
        progcnter += 1
except:
    print(regs)
