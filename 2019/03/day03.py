from collections import defaultdict

WIRE_1_BIT = 1
WIRE_2_BIT = 2
CROSSING = WIRE_1_BIT | WIRE_2_BIT


grid = defaultdict(lambda: {'c': 0, WIRE_1_BIT: 0, WIRE_2_BIT:0})

def parse(s):
    cmds = s.split(',')
    p = lambda x: (x[0], int(x[1:]))
    return [p(cmd) for cmd in cmds]

def modify_grid(cmds, BIT_TO_SET):
    global grid
    x, y, steps = 0, 0, 0
    for d, dis in cmds:
        for i in range(dis):
            if d == "U":
                y += 1 
            elif d == "D":
                y -= 1
            elif d == "L":
                x -= 1
            elif d == "R":
                x += 1
            steps += 1
            grid[(x,y)]['c'] = grid[(x,y)]['c'] | BIT_TO_SET
            if grid[(x,y)][BIT_TO_SET] == 0:
                grid[(x,y)][BIT_TO_SET] = steps

wire1 = parse(input())
wire2 = parse(input())

modify_grid(wire1, WIRE_1_BIT)
modify_grid(wire2, WIRE_2_BIT)

print(len(grid))

def part1():
    print("PART 1: ", min(abs(x) + abs(y) for (x,y),data in grid.items() if
        data['c'] == CROSSING and x != 0 and y != 0))
part1()

def part2():
    print("PART 2: ", min(data[WIRE_1_BIT] + data[WIRE_2_BIT] for (x,y),data in grid.items() if
        data['c'] == CROSSING and x != 0 and y != 0))



part2()
