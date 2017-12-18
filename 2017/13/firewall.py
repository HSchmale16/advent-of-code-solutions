import copy
import sys

def load_firewall(fname):
    poses = []
    depths = []
    with open(fname) as f:
        for line in f.readlines():
            pos, depth = (int(x) for x in line.split(':'))
            poses.append(pos)
            depths.append(depth)
    firewall = [None for i in range(max(poses) + 1)]
    for p,d in zip(poses, depths):
        firewall[p] = (0, d, True)
    return firewall,poses

def step_firewall(fwall):
    firewall, poses = fwall
    for i in poses:
        place, max_depth, down = firewall[i]
        if down:
            place += 1
        else:
            place -= 1
        if place == (max_depth - 1) or place == 0:
            down = not down
        firewall[i] = (place, max_depth, down) 
    return firewall, poses

def step_n(n, firewall):
    from_state = max(step_n.prevs)
    if n > from_state:
        steps = n - from_state
        firewall = step_n.prevs[from_state]
    else:
        return step_n.prevs[n] 
    for i in range(steps):
        firewall = step_firewall(firewall)
    step_n.prevs[n] = copy.copy(firewall)
    return firewall

def sim_firewall_run(delay, firewall):
    firewall = copy.deepcopy(firewall)
    firewall = step_n(delay, firewall)
    pentalty = 0
    for i in range(len(firewall[0])):
        if i in firewall[1] and firewall[0][i][0] == 0:
            pentalty += i * firewall[0][i][1]
            if pentalty != 0:
                break
        firewall = step_firewall(firewall)
    return pentalty
def main():
    firewall = load_firewall(sys.argv[1])
    step_n.prevs = {0: copy.copy(firewall)}

    for i in range(20000):
        pen = sim_firewall_run(i, firewall)
        print(i, pen)
        if pen == 0:
            break

if __name__ == '__main__': main()
