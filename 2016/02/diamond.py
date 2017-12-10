import sys

keypad = [
    [0, 0, 1, 0, 0],
    [0, 2, 3, 4, 0],
    [5, 6, 7, 8, 9],
    [0, 'A', 'B', 'C', 0],
    [0, 0, 'D', 0, 0]
]

def lock(x, y, dx, hor=False):
    widths = [(2, 2), (1, 3), (0, 4), (1, 3), (2, 2)]
    l, h = widths[y]
    v = x + dx
    print('lock', v, l, h)
    if v <= l: return l
    elif v >= h: return h 
    return v

def go_dir(x, y, dr):
    if   dr == 'L': x = lock(x, y, -1, True)
    elif dr == 'R': x = lock(x, y,  1, True)
    elif dr == 'U': y = lock(y, x, -1)
    elif dr == 'D': y = lock(y, x,  1)
    return x, y

def exec_line(line, x, y):
    for c in line:
        x, y = go_dir(x, y, c)
        print(c, x, y)
    print() 
    return x, y

def main():    
    x, y = (0, 2)
    code = []
    with open(sys.argv[1]) as f:
        for line in f.readlines():
            x, y = exec_line(line, x, y)
            code.append(keypad[y][x])
            print(code)

if __name__ == '__main__':
    main()
