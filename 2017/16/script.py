import sys

max_char = sys.argv[2][0]

with open(sys.argv[1]) as f:
    instructions = f.read().split(',')
    instructions[-1] = instructions[-1].strip()

dancers = [chr(i) for i in range(ord('a'), ord(max_char) + 1)]

def do_dance(dancers):
    for instruct in instructions:
        cmd = instruct[0]
        if cmd == 's':
            # SPIN
            times = int(instruct[1:])
            dancers = dancers[-times:] + dancers[0:-times]
        elif cmd == 'x':
            # EXCHANGE POS
            a, b = tuple(map(int, instruct[1:].split('/')))
            dancers[a], dancers[b] = dancers[b], dancers[a] 
        elif cmd == 'p':
            # EXCHANGE BY VALUE
            a, b = tuple(map(dancers.index, instruct[1:].split('/')))
            dancers[a], dancers[b] = dancers[b], dancers[a] 
    return dancers

def join(dancers):
    return ''.join(dancers)

do_x_times = 1_000_000_000
previous = {}
for i in range(1000):
    jd = join(dancers)
    if jd in previous:
        times = i - previous[jd]
        print(i, times)
        break
    else:
        previous[jd] = i
    dancers = do_dance(dancers)

target = (do_x_times - 1) % times
print(target)

for k, v in previous.items():
    if v == target:
        print(k)
