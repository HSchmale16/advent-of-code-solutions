import sys
import numpy as np

def get_idxs(ifrom, length, wrap):
    return [i % wrap for i in range(ifrom, ifrom + length)]  


def day10hash(lengths, circ_len=5):
    skip = 0
    A = np.array(list(range(circ_len)))
    position = 0
    for length in lengths:
        idxs = get_idxs(position, length, circ_len)
        x = np.take(A, idxs, mode='wrapped')
        np.put(A, idxs, x[::-1], mode='wrapped')
        position += skip + length
        skip += 1
    return A

with open(sys.argv[1]) as f:
    arr = [int(x) for x in f.read().split(',')]
    print(arr)
    print(day10hash(arr, 256))
