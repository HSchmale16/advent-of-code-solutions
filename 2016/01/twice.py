import sys
import matplotlib.pyplot as plt

def split_cmd(x):
    return (x[:1], int(x[1:]))

def turn_left(x):
    if x == 0:
        return 3
    return (x - 1) % 4
    
def turn_right(x):
    return (x + 1) % 4

 
dx, dy = 0, 0
direct = 0
places_visited = [(0, 0)]

string = []
with open(sys.argv[1]) as f:
    string = map(str.strip, f.read().split(','))

for cmd in string:

    turn, length = split_cmd(cmd)
    if turn == 'R':
        direct = turn_right(direct)
    else:
        direct = turn_left(direct)


    if direct == 0:
        dy += length
    elif direct == 1:
        dx += length
    elif direct == 2:
        dy -= length
    elif direct == 3:
        dx -= length
    

    coord = (dx, dy)
    places_visited.append(coord)

x = [x[0] for x in places_visited]
y = [x[1] for x in places_visited]

plt.plot(x,y)
plt.show()
