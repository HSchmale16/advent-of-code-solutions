from collections import Counter
initial_state = [int(x) for x in input().split(",")]

current_state = Counter(initial_state)
for i in range(256):
    next_state = Counter()
    for spawn, count in current_state.items():
        if spawn == 0:
            next_state[8] += count
            next_state[6] += count
        else:
            next_state[spawn - 1] += count
    current_state = next_state
    if i == 79 or i == 255:
        print(sum(current_state.values()))


#for i in range(256):
#    new_fishes = []
#    for i in range(len(state)):
#        if state[i] == 0:
#            new_fishes.append(8)
#            state[i] = 7
#        state[i] -= 1
#    state.extend(new_fishes)
#print(len(state))
