def max_element(l):
    mx = max(l)
    idx = -1
    for i,v in enumerate(l):
        if idx > -1 and v == mx: return idx, 0
        if v == mx:  idx = i 
    return idx, 1

seen = set()

with open('input') as f:
    memcells = list(map(int, f.read().split()))
#    memcells = [0, 2, 7, 0]
    seen.add(tuple(memcells))
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
        print(memcells, sum(memcells))
        count += 1
        if tuple(memcells) in seen: break
        seen.add(tuple(memcells))
print(count)
