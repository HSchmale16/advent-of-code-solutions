
original = [int(x) for x in input().split(',')]

def intcode(noun, verb):
    s = [x for x in original]
    s[1] = noun
    s[2] = verb
    i = 0
    while s[i] != 99:
        if s[i] == 1:
            s[s[i+3]] = s[s[i+1]] + s[s[i+2]] 
        elif s[i] == 2:
            s[s[i+3]] = s[s[i+1]] * s[s[i+2]] 
        else:
            pass
        i+=4

    return s[0]

target = 1960720

for i in range(0,100):
    for j in range(0,100):
        res = intcode(i, j)
        print(i,j, res, 100*i+j)
