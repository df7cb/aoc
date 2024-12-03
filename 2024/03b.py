#!/usr/bin/python3

import re

active = True
sum = 0

with open("03.txt") as f:
    for line in f:
        for cmd in re.findall(r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)", line):
            if cmd == "do()":
                active = True
            elif cmd == "don't()":
                active = False
            elif active:
                m = re.match(r'mul\((\d{1,3}),(\d{1,3})\)', cmd)
                a, b = m.groups()
                print(a, b)
                sum += int(a) * int(b)

print(sum)
