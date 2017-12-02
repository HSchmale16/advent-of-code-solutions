import sys

keypad = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def lock(x, dx):
    y = x + dx
    if y < 0: return 0
    if y > 2: return 2
    return y

def go_dir(dx, dy, dr):
    if   dr == 'L': dx = lock(dx, -1)
    elif dr == 'R': dx = lock(dx, 1)
    elif dr == 'U': dy = lock(dy, -1)
    elif dr == 'D': dy = lock(dy, 1)
    return dx, dy

def exec_line(line, dx, dy):
    dx, dy = (1, 1)
    for c in line:
        dx, dy = go_dir(dx, dy, c) 
    return dx, dy
        
dx, dy = (1, 1)
code = []
with open(sys.argv[1]) as f:
    for line in f.readlines():
        dx, dy = exec_line(line, dx, dy)
        code.append(keypad[dy][dx])
        print(code)

