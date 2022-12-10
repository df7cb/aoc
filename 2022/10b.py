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

for cycle in range(1, 241):
    pixel = (cycle - 1) % 40
    if cycles[cycle] - 1 <= pixel <= cycles[cycle] + 1:
        print('#', end='')
    else:
        print('.', end='')

    if pixel == 39:
        print()

