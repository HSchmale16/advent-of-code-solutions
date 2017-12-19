import operator
import sys
import numpy as np
from functools import reduce
from collections import deque

def get_idxs(ifrom, length, wrap):
    return [i % wrap for i in range(ifrom, ifrom + length)]  

def calc_dense_hash(A):
    dense = []
    for i in range(0, len(A), 16):
        dense.append(reduce(operator.xor, A[i+1:i+16], A[i]))
    return dense 

def dense_to_str(dense):
    return ''.join('{0:02x}'.format(i) for i in dense)

def knot_hash(lengths, circ_len=5):
    lengths += [17, 31, 73, 47, 23]
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

def blob_count(grid):
    count = 0
    def dfs(labels, r, c, n):
        if not (0 <= r < 128 and 0 <= c < 128): return
        if grid[r][c] == '1' and labels[r,c] == 0:
            labels[r,c] = n
            dfs(labels, r + 1, c, n)
            dfs(labels, r - 1, c, n)
            dfs(labels, r, c + 1, n)
            dfs(labels, r, c - 1, n)
    labels = np.zeros(128 * 128).reshape(128, 128).astype(int) 
    for r in range(128):
        for c in range(128):
            if grid[r][c] == '1' and labels[r,c] == 0:
                count += 1
                dfs(labels, r, c, count)
    return count, labels 
 

def bin_hash(h):
    b = bin(int(h, 16))[2:]
    return b.rjust(128, '0')

def main():
    key = 'oundnydw'
    b = []
    for i in range(128):
        hash_in = [ord(i) for i in '{}-{}'.format(key, i)]
        h = knot_hash(hash_in, 256)
        bstr = bin_hash(h) 
        b.append(bstr)
    print(len(b), len(b[0]))
    print(blob_count(b)) 

if __name__ == '__main__':
    main()
