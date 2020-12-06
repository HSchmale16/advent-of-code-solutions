import sys

def seat_id(row, col):
    return row * 8 + col


def bin_part(spec, g_high, go_low, go_high):
    low, high =  0, g_high
    for c in spec:
        if c == go_low:
            high -= (high - low) // 2
        elif c == go_high: 
            low += (high - low) // 2
    return (low, high)[spec[-1] == go_high]

def compute_seat_id_from_spec(spec):
    row = bin_part(spec[:7], 128, 'F', 'B')
    col = bin_part(spec[7:], 7, 'L', 'R')
    return seat_id(row, col)


if __name__ == '__main__':
    lines = [line.strip() for line in sys.stdin.readlines()]

    seat_ids = set(map(compute_seat_id_from_spec, lines))
    
    # Part 1 
    print(max(seat_ids))

    # Part 2
    all_seats = set(range(min(seat_ids), max(seat_ids)))
    missing_seats = all_seats - seat_ids
    print(missing_seats) 


