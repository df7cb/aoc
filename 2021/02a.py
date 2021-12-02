#!/usr/bin/python3

import re

x, y = 0, 0

with open('02.txt') as f:
    for line in f:
        if m := re.match('forward (\d+)', line):
            x += int(m.group(1))
        elif m := re.match('up (\d+)', line):
            y -= int(m.group(1))
        elif m := re.match('down (\d+)', line):
            y += int(m.group(1))
        else:
            print("Cannot navigate", line)

print(x, y, x*y)
