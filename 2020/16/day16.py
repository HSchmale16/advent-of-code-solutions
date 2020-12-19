import sys

def mk_crit(line):
    print(line)
    desc, crit = line.split(':')
    part_a, part_b = crit.split("or")
    a, b = map(int, part_a.split('-'))
    c, d = map(int, part_b.split('-'))
    return desc, lambda x: a <= x <= b or c <= x <= d

def invalid_nums(nums, crits):
    invalids = []
    for num in nums:
        if not any(map(lambda c: c(num), crits)):
            invalids.append(num)

    return invalids


descs, crits = [], []
while (line := input().strip()) != "":
    line = line.strip()
    d, c = mk_crit(line)
    descs.append(d)
    crits.append(c)

# skip desc
input()

my_ticket_nums = [int(x) for x in input().split(',')]
input()
input()
print(my_ticket_nums)

invalids = []
for line in sys.stdin.readlines():
    current_num = [int(x) for x in line.split(',')]
    invalids.extend(invalid_nums(current_num, crits))

print("Part 1: ", sum(invalids))
