def fuel(targets, pos):
    total = 0
    for target in targets:
        diff = target - pos
        total += abs(diff)
    return total

def fuel2(targets, pos):
    total = 0
    for target in targets:
        diff = abs(target - pos)
        total += int((diff * (diff + 1)) / 2)
        
    return total
    

x = list(map(int, input().split(',')))
low, high = min(x), max(x)

def part1():
    r = range(low, high + 1)
    print(min(map(lambda t: fuel(x, t), r)))

def part2():
    r = range(low, high + 1)
    print(min(map(lambda t: fuel2(x, t), r)))

part1()
part2()
