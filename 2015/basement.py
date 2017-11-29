f = 0
for i,c in enumerate(input()):
    if f == -1:
        raise ValueError(i)
    if c == ')' :
        f -= 1
    else:
        f += 1
print(f)
