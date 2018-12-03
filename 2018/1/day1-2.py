with open('input.txt') as f:
    seen_numbers = set([0])
    value = 0
    numbers = [int(x) for x in f.readlines()]
    Seen = False 
    
    while not Seen:
        for number in numbers:
            value += number
            if value not in seen_numbers:
                seen_numbers.add(value)
            else:
                print(value)
                Seen = True
                break
