import re
import sys
from numpy import base_repr

# ruleNum -> str
rules = {}
tests = []
all_rules = False

for line in map(str.strip, sys.stdin.readlines()):
    if line == "":
        all_rules = True
        continue
    if not all_rules:
        num, rule = line.split(":");
        rules[num] = rule.strip() 
    else:
        tests.append(line)

# Apply part 2 replacement rules
#rules["8"] = "42 | 42 8"
#rules["11"] = "42 31 | 42 11 31"

# Rules Translation
rule_names = ["A" + base_repr(x, base=10) for x in range(150)]


# Translate the rules to a series of numbers.
print("Day19_2 {")
for k, v in rules.items():
    l = []
    for s in v.split(" "):
        if s.isnumeric():
            l.append(rule_names[int(s)])
        else:
            l.append(s)
    print(rule_names[int(k)], " = ", ' '.join(l))
print("}")

with open('tests.txt', 'w') as f:
    for t in tests:
        print(t, file=f)
