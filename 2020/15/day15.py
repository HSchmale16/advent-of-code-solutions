from sys import argv
from collections import Counter

class TwoBuffer:
    def __init__(self, first):
        self.nums = [first, first]

    def push(self, new):
        self.nums[1] = self.nums[0]
        self.nums[0] = new

    def val(self):
        return self.nums[0] - self.nums[1]

    def __str__(self):
        return str(self.nums)

l = [int(x) for x in input().split(",")]

n = int(argv[1])
c = Counter(l)
last_seen = {k:TwoBuffer(v) for v,k in enumerate(l)}

next_value = l[-1] # start with the last value seen
for i in range(len(l), n):
    last_num = next_value
    if c[last_num] == 1:
        next_value = 0
    else:
        next_value = last_seen[last_num].val()
    c[next_value] += 1
    if next_value in last_seen:
        last_seen[next_value].push(i)
    else:
        last_seen[next_value] = TwoBuffer(i)
print(next_value)
