with open('input') as f:
    dMinMax = lambda a: max(a) - min(a)
    lineToNums = lambda line: map(int, line.split())
    sum(map(dMinMax, map(lineToNums, f.readlines())))
