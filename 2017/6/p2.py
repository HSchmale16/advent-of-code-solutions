def max_element(l):
    mx = max(l)
    idx = -1
    for i,v in enumerate(l):
        if idx > -1 and v == mx: return idx, 0
        if v == mx:  idx = i 
    return idx, 1

seen = {}

with open('input') as f:
    memcells = list(map(int, f.read().split()))
#    memcells = [0, 2, 7, 0]
    seen[tuple(memcells)] = 0
    count = 0
    sm = sum(memcells)
    while True:
        mxe, new = max_element(memcells)
        cur = mxe
        distrib = memcells[mxe]
        memcells[mxe] = 0
        while distrib > 0:
            cur = (cur + 1) % len(memcells)
            if new == 1 and cur == mxe: continue
            memcells[cur] += 1
            distrib -= 1
        count += 1
        if tuple(memcells) in seen:
            print(count - seen[tuple(memcells)])
            break
        seen[tuple(memcells)] = count
print(count)
