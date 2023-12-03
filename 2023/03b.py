#!/usr/bin/python3

import re

engine = []

with open("03.txt") as f:
    for line in f:
        engine.append(line.strip())

gears = {}

def scan(y, x, l, part):
    for y0 in range(max(0, y-1), min(len(engine), y+1+1)):
        for x0 in range(max(0, x-1), min(len(engine[0]), x+1+l)):
            symbol = engine[y0][x0]
            if symbol == '*':
                print(symbol)
                if (y0, x0) not in gears:
                    gears[(y0, x0)] = []
                gears[(y0, x0)].append(int(part))

for y in range(len(engine)):
    for m in re.finditer('(\d+)', engine[y]):
        part = m.group(1)
        print(part, m.start(1))
        scan(y, m.start(1), len(part), part)

print(gears)

ratios = 0

for gear in gears.values():
    if len(gear) != 2:
        continue
    print(gear)
    ratios += gear[0] * gear[1]

print(ratios)
