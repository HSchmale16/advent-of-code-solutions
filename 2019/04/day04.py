def ascending_check(a, b, c, d, e, f):
    return a <= b <= c <= d <= e <= f

def two_matches(a, b, c, d, e, f):
    return a == b or b == c or c == d or d == e or e == f

def not_larger_group(s):
    runs = []
    last_chr, run = '0', 0
    for c in s:
        if c != last_chr:
            runs.append((last_chr, run))
            run = 1
        else:
            run += 1
        last_chr = c
    runs.append((last_chr, run))
    print(runs)
    return len([r for _, r in runs if r == 2]) >= 1



low, high = map(int, input().split("-"))
print(low, high)

print(not_larger_group(list("112233")) == True)
print(not_larger_group(list("123444")) == False)
print(not_larger_group(list("111122")) == True)

count = 0
for i in range(low, high + 1):
    s = list(str(i))
    if ascending_check(*s) and two_matches(*s) and not_larger_group(s):
        count += 1

print("DAY 04 PART 1 = ", count)
