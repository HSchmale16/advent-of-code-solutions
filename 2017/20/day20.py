import re

pattern = re.compile("(\d)+")

def readParticle(line):
    n = readParticle.n
    readParticle.n += 1
    return (n, [int(x) for x in pattern.findall(line)])
readParticle.n = -1

def accelValue(p):
    p1 = p[1]
    return p1[6] * p1[6] + p1[7] * p1[7] + p1[8] * p1[8]

with open("input.txt") as f:
    particles = [readParticle(line) for line in f.readlines()]

# Part 1
l = (sorted(particles, key=accelValue))
print(l[-1])

# Part 2


