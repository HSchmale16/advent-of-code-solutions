from blist import blist

def lock_range(i, forward, maxlen):
    return (i + forward) % maxlen

array = blist([0])
curpos = 0
steps = 328
max_value = 50_000_001

for i in range(1, max_value):
    curpos = lock_range(curpos, steps, len(array))
    array.insert(curpos + 1, i)
    curpos = array.index(i)
    if i % 100000 == 0: print(i)

print(array[array.index(0) + 1]) 
