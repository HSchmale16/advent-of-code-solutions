with open('input') as f:
 
    for line in f.readlines():
        l, u = tuple(map(int, line.strip().split('-')))
        
