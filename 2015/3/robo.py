import sys

def go_dir(c, dx, dy):
    if   c == '^': dy += 1
    elif c == 'v': dy -= 1
    elif c == '<': dx -= 1
    elif c == '>': dx += 1
    return dx, dy

santas = [(0, 0) for i in range(2)]
houses = {(0,0)}
with open(sys.argv[1]) as f:
    for i,c in enumerate(f.read()):
        a = i % 2
        santas[a] = go_dir(c, *santas[a]) 
        [houses.add(i) for i in santas]

print(len(houses))
