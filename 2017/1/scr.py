with open("input") as f:
    x = f.read().strip()
    a = [int(c) for c in x]
    s = 0
    for i in range(-1, len(a) - 1):
        if a[i] == a[i+1]:
            s += a[i]
print(s)
