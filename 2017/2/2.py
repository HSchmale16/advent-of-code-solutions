def divisible(a):
    for i in a:
        for j in a:
            if i == j:
                continue
            if i % j == 0:
                return i / j


with open('input') as f:
    s = 0
    ss = []
    for line in f.readlines():
        a = map(int, line.split())
        ss.append(divisible(a))
    print(sum(ss))
