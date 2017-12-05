start = 20151125
t_row = 3010
t_col = 3019
multiply = 252533
modulus = 33554393

def code():
    code.last = code.last * multiply % modulus
    return code.last
code.last = start 


max_row = 2
row, col = (2, 1)

while True:
    print(row,col,code())
    if row == t_row and col == t_col:
        break
    row -= 1
    col += 1
    if row == 0:
        max_row += 1
        row = max_row
        col = 1 
