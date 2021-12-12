#!/usr/bin/python3

import re

paths = {}

with open('12.txt') as f:
    for line in f:
        m = re.match('(.+)-(.+)', line)
        if m.group(1) not in paths:
            paths[m.group(1)] = set()
        paths[m.group(1)].add(m.group(2))
        if m.group(2) not in paths:
            paths[m.group(2)] = set()
        paths[m.group(2)].add(m.group(1))

print(paths)

nr = 1
def walk(seen, here, to):
    global nr
    if here == 'end':
        print(nr, seen)
        nr += 1
        return
    for next in paths[here]:
        if next not in seen or next.upper() == next:
            walk(seen + [next], next, to)

walk(['start'], 'start', 'end')
