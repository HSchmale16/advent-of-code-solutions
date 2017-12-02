import sys

PC = 0
instructions = []
registers = {}

def exec(cmd):
    pass    

with open(sys.argv[1]) as f:
    instructions = map(str.split,f.readlines())
