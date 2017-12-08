import sys
from itertools import permutations

values = []
with open(sys.argv[1]) as f:
    values = [int(x) for x in f.readlines()]

 
