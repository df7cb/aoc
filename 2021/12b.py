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
def walk(seen, lower2, here, to):
    global nr
    if here == 'end':
        print(nr, seen)
        nr += 1
        return
    for next in paths[here]:
        if next not in seen or next.upper() == next:
            walk(seen + [next], lower2, next, to)
        elif lower2 is None and next.lower() == next and next not in ('start', 'end'):
            walk(seen + [next], next, next, to)

walk(['start'], None, 'start', 'end')
