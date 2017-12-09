import sys

with open(sys.argv[1]) as f:
    stream = f.read()

score = 0
depth = 0
garbage_count = 0
skip_next = False
garbage = False

for c in stream:
    if skip_next:
        skip_next = False
        continue
    if c == '!': 
        skip_next = True 
    elif c == '{' and not garbage:
        depth += 1
    elif c == '}' and not garbage:
        score += depth
        depth -= 1
    elif c in '<>': 
        if c == '<':
            if garbage:
                garbage_count += 1
            garbage = True
        else:
            garbage = False
    elif garbage:
        garbage_count += 1

print(score)
print(garbage_count)
