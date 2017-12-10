import itertools
import operator

class SpiralGen(object):
    def __init__(self, n):
        self.n = n
        self.num = 0
        self.last = 0
        self.count = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        self.count += 1
        if self.count > self.n:
            raise StopIteration()
        if self.num == self.last:
            self.last = self.num
            self.num += 1
            return self.num
        self.last = self.num
        return self.num 

def calcCoords(index):
    x, y = (0, 0)
    n = 0
    current_pos = 0 
    gen = SpiralGen(index)
    dv = 0
    direction = 0
    while current_pos < index:
        direction = n % 4
        last, dv = dv, next(gen)
        current_pos += dv
        if direction == 0:
            x += dv 
        elif direction == 1:
            y += dv
        elif direction == 2:
            x -= dv 
        else:
            y -= dv
        n += 1
    dv = current_pos - index
    if direction == 0:
        x -= dv
    elif direction == 1:
        y -= dv
    elif direction == 2:
        x += dv 
    else:
        y += dv
    return x,y

puzin = 265149
memgrid = {(0,0): 1}

def get_value(memgrid, pos):
    deltas = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,1), (1,0), (1,-1)]
    s = 0
    for i in deltas:
        pos2 = tuple(map(operator.add, pos, i))
        if pos2 not in memgrid:
            continue
        s += memgrid[pos2]
    return s

for i in range(1,puzin):
    x, y = calcCoords(i)
    value = get_value(memgrid, (x,y))
    if value > puzin:
        print(value)
        break
    memgrid[x,y] = value




