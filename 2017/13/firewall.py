import copy
import sys
from functools import reduce

def load_firewall(fname):
    with open(fname) as f:
        wall = {}
        for line in f.readlines():
            pos, depth = (int(x) for x in line.split(':'))
            wall[pos] = (0, depth - 1, True)
    return wall

def print_firewall(wall):
    rows = reduce(lambda a, x: max(a, x[1] + 1), wall.values(), 0) + 1
    screen = ['' for i in range(rows)]
    screen[0] = ''.join([f' {i}  ' for i in range(max(wall) + 1)])
    for i in range(max(wall) + 1):
        for j in range(1, rows):
            if i in wall:
                if wall[i][1] >= (j - 1):
                    screen[j] += '[S] ' if wall[i][0] == (j - 1) else '[ ] '
                else:
                    screen[j] += '    '

            else:
                screen[j] += '    '
    [print(i) for i in screen]

def step_firewall(fwall):
    for k, v in fwall.items():
        pos, depth, down = v
        if down:
            pos += 1
        else:
            pos -= 1
        if pos == depth or pos == 0:
            down = not down
        fwall[k] = (pos, depth, down)
    return fwall

def sim_firewall_run(delay, wall):
    if (delay - 1) == sim_firewall_run.last_delay:
        wall = step_firewall(sim_firewall_run.last_wall)
    else:
        for i in range(delay):
            wall = step_firewall(wall)
    sim_firewall_run.last_wall = dict(wall)
    sim_firewall_run.last_delay = delay
    severity = 0
    for i in range(max(wall) + 1):
        if i in wall and wall[i][0] == 0:
            severity += i * (wall[i][1] + 1) + 1
            break
        wall = step_firewall(wall)
        #print_firewall(wall)
    return severity
sim_firewall_run.last_wall = None
sim_firewall_run.last_delay = 0

def main():
    firewall = load_firewall(sys.argv[1])
    #sim_firewall_run(1, firewall)

    #"""
    delay = 0
    while True:
        pen = sim_firewall_run(delay, dict(firewall))
        print(pen, delay)
        if pen == 0:
            print(pen, delay)
            break
        delay += 1
    #"""

if __name__ == '__main__': 
    main()
