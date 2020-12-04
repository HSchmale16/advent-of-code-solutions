import sys
import re

def clear_it():
    global valid1, valid2, s
    if len(s) > 7 or (len(s) == 7 and 'cid' not in s):
        valid1 += 1
    else:
        s = dict()
        return
    i = 0
    for k,v in s.items():
        if k == 'cid':
            continue
        if KEYS[k](v):
            i += 1
    valid2 += (i == 7) 
    s = dict()

def chk_hgt(x):
    try:
        y = int(x[:-2])
        if x[-2:] == 'cm':
            return 150 <= y <= 193
        elif x[-2:] == 'in':
            return 59 <= y <= 76
    except ValueError:
        return False

KEYS = {
    'byr': lambda x: 1920 <= int(x) <= 2002,
    'iyr': lambda x: 2010 <= int(x) <= 2020,
    'eyr': lambda x: 2020 <= int(x) <= 2030,
    'hgt': chk_hgt,
    'hcl': lambda x: re.match('^#[0-9a-f]{6}$', x),
    'ecl': lambda x: x in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl',
        'oth'),
    'pid': lambda x: re.match('^\d{9}$', x)
}


s = dict()
valid1, valid2,i = 0,0,0
for line in sys.stdin.readlines():
    line = line.strip()
    if line == "":
        clear_it()
        continue
    fields = line.split(" ")
    for field in fields:
        k, v = field.split(":")
        s[k] = v
clear_it()
print(valid1, valid2) 
