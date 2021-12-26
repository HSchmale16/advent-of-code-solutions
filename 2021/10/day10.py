from sys import stdin
import statistics

def syntax_check(line):
    stack = []
    for c in line:
        if c in '([{<':
            stack.append(c)
        else:
            match = stack.pop()
            if c == ')' and match != '(':
                return 3, None
            if c == ']' and match != '[':
                return 57, None
            if c == '}' and match != '{':
                return 1197, None
            if c == '>' and match != '<':
                return 25137, None
    stack.append(match)
    return 0, stack

def complete_syntax(stack):
    score = 0
    print(stack)
    while len(stack) != 0:
        c = stack.pop()
        score *= 5
        if c == '(':
            score += 1
        elif c == '[':
            score += 2
        elif c == '{':
            score += 3
        elif c == '<':
            score += 4
        else:
            print("ERR")
    return score

lines = [l for l in stdin.readlines()]


part1, part2 = 0, [] 
for line in lines:
    score, remaining = syntax_check(line)
    part1 += score
    if score == 0:
        complete_score = complete_syntax(remaining)
        part2.append(complete_score)

print(part1)
print(statistics.median(part2))
