import sys
import re

RE = r"(.+) contain ((\d+) (.+)(?:, (\d+) (.+))+|no other bags)"
RE = re.compile(RE)

def make_list(line):
    m = RE.match(line)
    print(m.groups())

lines = [make_list(l.strip()) for l in sys.stdin.readlines()]


