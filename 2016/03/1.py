x = []
for line in open('input').readlines():
    nums = sorted(map(int, line.split()))
    if nums[0] + nums[1] > nums[2]: x.append(1)
print(sum(x))  
