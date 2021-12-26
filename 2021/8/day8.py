import sys

def what_digit(digit, wires):
    if len(digit) == 2:
        return "1"
    if len(digit) == 3:
        return "7"
    if len(digit) == 7:
        return "8"
    if len(digit) == 4:
        return "4"

    digit_set = set(digit)
    if len(digit) == 5:
        if digit_set == set("cdfbe"):
            return "5"
        if digit_set == set("gcdfa"):
            return "2"
        if digit_set == set("fbcad"):
            return "3"
    if len(digit) == 6:
        if digit_set == set("cefabd"):
            return "9"
        if digit_set == set("cdfgeb"):
            return "6"
        if digit_set == set("cagedb"):
            return "0"


part1 = 0
lines = [line.split('|') for line in sys.stdin.readlines()]
for wires_part, digits_part in lines:
    digits = digits_part.split()
    output_str = ""
    for digit in digits:
        output_str += what_digit(digit, wires_part)
        if len(digit) in [2,3,4,7]:
            part1 += 1
    print(int(output_str))

print(part1)

