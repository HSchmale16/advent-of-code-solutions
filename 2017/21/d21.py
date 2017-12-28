import sys
import numpy as np


def state2np(state):
    shape = state.count('/') + 1
    mp = {'.': 0, '#': 1}
    arr = np.array([mp[x] for x in state if x in mp]).reshape(shape, shape)
    arr.flags.writable = False
    return arr

def gen_rot_fp(arr):
    s = set()

    # Do rotations
    x = np.rot90(np.copy(arr))
    print(tuple(x))
    for i in range(3):
        x = np.rot90(np.copy(x))

def load_mappings(f):
    map2 = {}
    for line in f.readlines():
        frm, to = map(state2np, line.split('=>'))
    return map2

def main():
    gen_rot_fp(np.array([0,1,0,0,0,1,1,1,1]).reshape(3,3))
    #with open(sys.argv[1]) as f:
    #    mappings = load_mappings(f)
    


if __name__ == '__main__':
    main()