from collections import Counter

def line_check(line):
    words = []
    for word in line.split():
        cnt = Counter(word)
        if cnt in words:
            return 0
        words.append(cnt)
    return 1

with open('input') as f:
    print(sum(map(line_check, f.readlines())))
