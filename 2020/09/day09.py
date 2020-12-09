import sys
from itertools import combinations, accumulate

preamble = 25
seq = [int(x) for x in sys.stdin.readlines()]

for i,v in enumerate(seq[preamble:], start=preamble):
    good_value = False
    for a,b in combinations(seq[i-preamble:i], 2):
        if a + b == v:
            good_value = True
            break
    if not good_value:
        break
print("Part 1 = ", v)

target_sum = v

min_window_size = 2
done = False
for window in range(min_window_size, preamble*3):
    for i in range(window-1, len(seq)):
        seq2 = seq[i-window:i+1]
        if sum(seq2) == target_sum:
            print(seq2, window, i)
            low, high = min(seq2), max(seq2)
            print(low, high)
            print("Part 2 = ", low + high) 


