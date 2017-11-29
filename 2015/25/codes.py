start = 20151125
t_row = 3010
t_col = 3019
multiply = 252533
modulus = 33554393

def code(x):
    code.last = x * multiply % modulus
    return code.last
code.last = start

row = 1
current = (0,0)
n = 0 
