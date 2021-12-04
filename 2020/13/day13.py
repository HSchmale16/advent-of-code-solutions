arrival = int(input())
bus_index = [(i,int(x)) for i,x in enumerate(input().split(",")) if x != 'x']
buses = [x[1] for x in bus_index]
ts = [0 for x in buses]

#done = False
#while not done:
#    ts = [x + y for x,y in zip(buses, ts)]
#    for i,v in enumerate(ts):
#        if v >= arrival:
#            print("Part 1", (v - arrival) * buses[i])
#            done = True
#            break

ts = 12 #100000000000001
my_divmod = lambda y: divmod(ts, y)
done = False
while not done:
    timestamps = [my_divmod(x) for x in buses]
    i = 0
    for (bus,the_id),(div,mod) in zip(bus_index, timestamps):
        if (mod + bus) == the_id:
            break
        i += 1
        pass
    if i >= len(buses):
        done = True
print(ts)
