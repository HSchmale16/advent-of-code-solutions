puzin = str(1113122113)

def look_say(x):
    run_ls = []
    run = 1
    last = x[0]
    if len(x[1:]) == 0:
        run_ls = [(run,last)]
    for i in x[1:]:
        if i == last:
            run += 1
        else:
            run_ls.append((run, last))
            run = 1
            last = i
    # LAST LENGTH
    run_ls.append((run, last))
    run = 1
    last = i
    # BUILD STR 
    res = ""
    for i in run_ls:
        res += str(i[0]) + str(i[1])
    return res


for i in range(50):
    puzin = look_say(puzin)
print(len(puzin))
