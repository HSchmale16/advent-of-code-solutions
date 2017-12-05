import json

def sum_nums(j):
    if type(j) == int or type(j) == float:
        return j
    elif type(j) == list:
        return sum(map(sum_nums, j))
    elif type(j) == dict:
        if "red" in j or "red" in j.values():
            return 0
        return sum(map(sum_nums, j.values()))
    return 0

with open('input') as f:
    print(sum_nums(json.load(f)))
