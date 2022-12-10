#!/usr/bin/python3

import re

x = 1
cycles = [x, x]

with open("10.txt") as f:
    for line in f:
        if re.match('^noop', line):
            cycles.append(x)
        elif m := re.match('^addx ([-\d]+)', line):
            cycles.append(x)
            x += int(m.group(1))
            cycles.append(x)
print(cycles)

interesting = [20 + i*40 for i in range(6)]
print(interesting)

print([cycles[i] for i in interesting])
signal_strengths = [cycles[i] * i for i in interesting]
print(signal_strengths)
print(sum(signal_strengths))
