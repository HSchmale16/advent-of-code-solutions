import sys
from collections import Counter

def update_mask(line):
    _, __, letters = line.split(" ")
    letters_rev = reversed(letters)
    # [(bit_num, set_to)]
    return [(x,int(value)) for x,value in enumerate(letters_rev) if
            value != "0"]

def apply_mask(bit_val, mask, bin_val):
    s = ""
    i = 0
    bit_val = list(reversed(bin(bit_val)[2:]))
    for m,v in zip(reversed(mask), reversed(bin_val)):
        if m == "0":
            s += v
        elif m == "1":
            s += "1"
        else:
            s += "0" if i >= len(bit_val) else bit_val[i]
            i += 1

    return int(''.join(reversed(s)), 2)


def calc_addrs(value, mask):
    addrs = []
    # Pad to base 36
    value |= (1 << 37) 
    bin_val = bin(value)[4:]
    floating_count = mask.count("X")
    
    for i in range(2**floating_count):
        addrs.append(apply_mask(i, mask, bin_val))        

    return addrs

mem = {}
for line in sys.stdin.readlines():
    line = line.strip()
    if line.startswith("mask"):
        mask = line.split("=")[1].strip()
    else:
        start, end = line.index("[") + 1, line.index("]")
        addr = int(line[start:end])
        addrs = calc_addrs(addr, mask)
        value = int(line.split("=")[1])
        for a in addrs:
            mem[a] = value


print("Part 2: ", sum(mem.values()))
