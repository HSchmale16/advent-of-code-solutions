with open("input") as f:
    x = f.read().strip()
    a = [int(c) for c in x]
    s = 0
    mid = len(a) / 2
    f = a[:mid]
    l = a[mid:]
    for i,j in zip(f,l):
        if i == j:
            s += i
    for i,j in zip(l,f):
        if i == j:
            s += i
print(s)
