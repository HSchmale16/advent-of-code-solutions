arrival = int(input())
buses = [int(x) for x in input().split(",") if x != 'x']
ts = [0 for x in buses]

done = False
while not done:
    ts = [x + y for x,y in zip(buses, ts)]
    for i,v in enumerate(ts):
        if v >= arrival:
            print("Part 1", (v - arrival) * buses[i])
            done = True
            break
