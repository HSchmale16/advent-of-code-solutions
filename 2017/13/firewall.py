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


firewall = load_firewall(sys.argv[1])
print(firewall)
for i in range(4):
    firewall = step_firewall(firewall)
    print(firewall)

