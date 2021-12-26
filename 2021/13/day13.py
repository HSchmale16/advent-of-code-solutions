from sys import stdin

def apply_fold(coords, axis : str, loc : int):
    new_coords = set()
    for x,y in coords:
        if axis == 'x':
            new_x = x
            if loc < x:
                new_x = loc - (x - loc)
            elif loc == x:
                continue
            assert new_x < loc
            x = new_x
        else:
            new_y = y
            if loc < y:
                new_y = loc - (y - loc)
            elif loc == y:
                continue
            assert new_y < loc
            y = new_y
        new_coords.add((x,y))


    return new_coords

reading_nums = True

coords = set()
folds = []

for line in map(str.strip, stdin.readlines()):
    if reading_nums:
        if line == "":
            reading_nums = False
            continue
        x,y = map(int, line.split(","))
        coords.add((x,y))
    else:
        fold, along, coord = line.split()
        axis, loc = coord.split('=')
        loc = int(loc)
        folds.append((axis, loc))

coords = apply_fold(coords, folds[0][0], folds[0][1])
# Part 1
# print(len(coords))

for axis, loc in folds[1:]:
    coords = apply_fold(coords, axis, loc)


print("x,y")
for x,y in coords:
    print(f'{x},{y}')
# used R to actually plot it.
