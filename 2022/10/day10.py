import sys

targets = [20, 60, 100, 140, 180, 220]
cycle = 0
x = 1
pc = 1
strength = 0

cmds = [l.split() for l in sys.stdin.readlines()]

def proc_cycle():
    global strength
    if pc in targets:
        strength += pc * x
        #print(x, pc, strength)
    pixel = (pc-1) % 40
    if pixel == 0:
        print()
    c = '#' if pixel in [x-1, x, x+1] else '.'
    print(c, end='')

proc_cycle()
for c in cmds:
    if len(c) == 1:
        pc += 1
        proc_cycle()
    else:
        v = int(c[1])
        pc += 1
        proc_cycle()
        pc += 1
        x += v
        proc_cycle()

