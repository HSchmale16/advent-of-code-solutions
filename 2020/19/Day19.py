import re
import sys

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

has_digits = re.compile("([0-9]+)")

starting = rules["0"]
match = has_digits.search(starting)
while match:
    the_rule_to_apply = rules[match.group(0)]
    
    if the_rule_to_apply[0] == '"':
        the_replacement = the_rule_to_apply[1]
    else:
        the_replacement = "(?:" + the_rule_to_apply + ")" 
    b,e = match.span()

    starting = starting[:b] + the_replacement + starting[e:]
    print(starting)
    match = has_digits.search(starting)

the_regex = "^" + starting.replace(" ", "") + "$"

print(the_regex)
my_regex = re.compile(the_regex)

matches = [x for x in tests if my_regex.match(x)] 
print(len(matches))

print(matches)
