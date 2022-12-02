import sys
import os

total = 0
part2 = 0
i_win_conditions = [
    (0, 1),
    (1, 2),
    (2, 0)
]

for line in sys.stdin.readlines():
    a, B = line.split()
    a = ord(a) - ord('A')
    b = ord(B) - ord('X')
    total += 1 + b
    
    if a == b:
        total += 3
    elif (a, b) in i_win_conditions:
        total += 6
   
    
    # Rock > Paper Scissors

    if B == 'X':
        part2 += 0 + ((a - 1) % 3) + 1
    elif B == 'Y':
        part2 += 3 + (a + 1) 
    elif B == 'Z':
        part2 += 6 + ((a + 1) % 3) + 1

print(total)
print(part2)
