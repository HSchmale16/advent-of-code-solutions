def gen_die():
    i = 1
    while True:
        yield i
        i = (i % 100) + 1

def new_position(old, dice1, dice2, dice3):
    new = old + dice1 + dice2 + dice3
    return (new - 1) % 10 + 1

dice = gen_die()

p1_start = int(input().split()[-1])
p2_start = int(input().split()[-1])

pos = [p2_start, p1_start]
scores = [0, 0]
turn = 1

while True:
    d1, d2, d3 = next(dice), next(dice), next(dice)
    
    score = new_position(pos[turn%2], d1, d2, d3) 
    scores[turn%2] += score
    pos[turn%2] = score

    #print(d1, d2, d3, pos, scores)


    if scores[turn%2] >= 1000:
        break
    turn += 1

print(f"Part 1 {turn * 3 * min(scores)}")
