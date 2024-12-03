#!/usr/bin/python3

import re

sum = 0

with open("03.txt") as f:
    for line in f:
        for a, b in re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', line):
            print(a, b)
            sum += int(a) * int(b)

print(sum)
