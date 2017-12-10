import sys

def escape(s):
    n = ""
    for c in s:
        if c in '\\"':
            n += '\\'
        n += c
    return '"' + n + '"'

def main():
    code = 0
    actual = 0
    with open(sys.argv[1]) as f:
        for line in f.readlines():
            line = "".join(line.split())
            code += len(escape(line))
            actual += len(line)
    print(code - actual)

if __name__ == '__main__':
    main() 
