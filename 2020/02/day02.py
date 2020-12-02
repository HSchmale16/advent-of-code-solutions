import sys
from collections import Counter 

def valid(line):
    highlow, letter, password = line.split(" ")
    low, high = map(int, highlow.split("-"))

    chr_list = Counter(password)
    return low <= chr_list[letter[0]] <= high

def valid2(line):
    highlow, letter, password = line.split(" ")
    low, high = map(int, highlow.split("-"))
    low -= 1
    high -= 1
    letter = letter[0]
    
    return ((password[low] == letter) + (password[high] == letter)) == 1

s1, s2 = 0, 0
for line in sys.stdin.readlines():
    s1 += valid(line)
    v = valid2(line)
    s2 += v

print(s1, s2)
