import sys
x = [[], [], []]
for line in open(sys.argv[1]).readlines():
    [x[k].append(v) for k,v in enumerate(map(int, line.split()))]
y = sum(map(lambda x: [sorted(x[i:i+3]) for i in range(0,len(x),3)], x), [])
print(y)
z = map(lambda x: x[0] + x[1] > x[2], y)
print(sum(z))
