import operator
import sys
import numpy as np
from functools import reduce

def get_idxs(ifrom, length, wrap):
    return [i % wrap for i in range(ifrom, ifrom + length)]  


def day10hash1(lengths, circ_len=5):
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

def calc_dense_hash(A):
    dense = []
    for i in range(0, len(A), 16):
        dense.append(reduce(operator.xor, A[i+1:i+16], A[i]))
    return dense 

def dense_to_str(dense):
    return ''.join('{0:02x}'.format(i) for i in dense)

def day10hash2(lengths, circ_len=5):
    lengths += [17, 31, 73, 47, 23]
    print(lengths)
    skip = 0
    A = np.array(list(range(circ_len)))
    position = 0
    for i in range(64):
        for length in lengths:
            idxs = get_idxs(position, length, circ_len)
            x = np.take(A, idxs, mode='wrapped')
            np.put(A, idxs, x[::-1], mode='wrapped')
            position += skip + length
            skip += 1
    return dense_to_str(calc_dense_hash(A))

with open(sys.argv[1]) as f:
    arr = [ord(x) for x in f.read().strip()]
    print(len(arr))
    print(day10hash2(arr, 256))
