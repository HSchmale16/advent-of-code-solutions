with open('input') as f:
    last = 0
    for i in f.readlines():
        l, u = tuple(map(int, i.strip().split('-')))
        if l - last > 1:
            print(last)
        last = u


