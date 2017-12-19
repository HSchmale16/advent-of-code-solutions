import copy
import sys

def load_firewall(fname):
    with open(fname) as f:
        wall = {}
        for line in f.readlines():
            pos, depth = (int(x) for x in line.split(':'))
            wall[pos] = (0, depth - 1, True)
    return wall

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
    print(fwall)
    return fwall



def sim_firewall_run(delay, wall):
    pentalty = 0
    for i in range(max(wall)):
        try:
            if wall[i][0] == 0:
                pentalty += i * wall[i][1]
        except KeyError: pass
        wall = step_firewall(wall)
    return pentalty

def main():
    firewall = load_firewall(sys.argv[1])

    for i in range(20000):
        pen = sim_firewall_run(i, firewall)
        print(i, pen)
        if pen == 0:
            break

if __name__ == '__main__': main()
