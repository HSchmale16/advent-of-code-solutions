import sys
import operator
from functools import reduce

def index_of(board_nums, num):
    for i, b in enumerate(board_nums):
        if b == num:
            return i


def make_board(board_temp):
    board = reduce(operator.add, board_temp, []) 
    return (board, [0 for _ in range(25)])


def apply_number(board, num):
    i = index_of(board[0], num)
    if i is not None:
        board[1][i] = 1
        return board
    return board

def check_win(markers):
    # check rows:
    for i in range(5):
        if sum(markers[i:i+5]) == 5:
            return True
        if sum(markers[i:25:5]) == 5:
            return True
    return False

def compute_score(drawn, board_num):
    board = set(board_num)
    for d in drawn:
        if d in board_num:
            board.remove(d)
    return sum(board)


def load_boards():
    boards = []
    board_temp = []
    for line in map(str.strip, sys.stdin.readlines()):
        if line == "":
            if len(board_temp) > 0:
                boards.append(make_board(board_temp))
            board_temp = []
        else:
            board_temp.append([int(x) for x in line.split()])
    boards.append(make_board(board_temp))

    return boards


numbers = list(map(int, sys.stdin.readline().split(",")))
drawn = []
boards = load_boards()
won_boards = set()
for num_index, num in enumerate(numbers):
    drawn.append(num)
    for i, board in enumerate(boards):
        if i in won_boards:
            continue
        boards[i] = apply_number(board, num)
        if check_win(boards[i][1]):
            score = num * compute_score(drawn, boards[i][0])
            print(f'{num=} {score=} {i=}')
            won_boards.add(i)
            #sys.exit(0)


