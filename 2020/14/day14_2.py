import sys
from collections import Counter

def update_mask(line):
    _, __, letters = line.split(" ")
    letters_rev = reversed(letters)
    # [(bit_num, set_to)]
    return [(x,int(value)) for x,value in enumerate(letters_rev) if value != "X"]

def bitSet(og, position, value):
    if value == 1: 
        return og | (1 << position)
    else:
        return og & (~(1 << position))

def apply_mask(value : int,mask) -> int:
    for index,v in mask:
        value = bitSet(value, index, v)
    return value


mem = {}
for line in sys.stdin.readlines():
    line = line.strip()
    if line.startswith("mask"):
        mask = update_mask(line)
        print(mask)
    else:
        start, end = line.index("[") + 1, line.index("]")
        addr = int(line[start:end])
        value = int(line.split("=")[1])
        value2 = apply_mask(value, mask)
        mem[addr] = value2
        print(addr, value, value2)

print("Part 1: ", sum(mem.values()))
