#!/usr/bin/python3

import re

engine = []

with open("03.txt") as f:
    for line in f:
        engine.append(line.strip())

print(engine)

def scan(y, x, l):
    for y0 in range(max(0, y-1), min(len(engine), y+1+1)):
        for x0 in range(max(0, x-1), min(len(engine[0]), x+1+l)):
            symbol = engine[y0][x0]
            if symbol not in "0123456789.":
                print(symbol)
                return True
    return False

parts = 0

for y in range(len(engine)):
    for m in re.finditer('(\d+)', engine[y]):
        part = m.group(1)
        print(part, m.start(1))
        if scan(y, m.start(1), len(part)):
            parts += int(part)
        else:
            print("not part", part)

print(parts)
