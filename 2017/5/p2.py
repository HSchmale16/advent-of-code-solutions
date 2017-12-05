instuctions = []
with open('input') as f:
    map(lambda x: instuctions.append(int(x)), f.readlines())

cur_instruct = 0
count = 0

try:
    while True:
        if cur_instruct < 0:
            break
        jump = instuctions[cur_instruct]
        if jump >= 3:
            instuctions[cur_instruct] -= 1
        else:
            instuctions[cur_instruct] += 1
        # MOVE
        cur_instruct += jump
        count += 1
finally:
    print(count)
