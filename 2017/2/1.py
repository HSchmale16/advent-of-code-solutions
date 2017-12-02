with open('input') as f:
    s = 0
    ss = []
    for line in f.readlines():
        a = map(int, line.split())
        ss.append(max(a) - min(a))
    print(sum(ss))
