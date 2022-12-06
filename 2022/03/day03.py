import sys

score = 0
for line in map(str.strip, sys.stdin.readlines()):
    l = len(line) // 2
    e, f =  line[:l], line[l:]

    c = list(set(e).intersection(f))[0]
    if c.isupper():
        score += ord(c) - ord('A') + 27
    else:
        score += ord(c) - ord('a') + 1
    print(score)
