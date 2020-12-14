#!/usr/bin/python3

import re

mem = {}

with open('14.txt') as f:
    for line in f:
        if m := re.match('mask = (.+)', line):
            ones = int(m[1].replace('X', '0'), 2)
            zeroes = int(m[1].replace('X', '1'), 2)
            print(m[1], ones, zeroes)
        elif m := re.match('mem\[(\d+)\] = (\d+)', line):
            mem[m[1]] = (int(m[2]) & zeroes) | ones

for i in mem:
    print(i, mem[i])

print(sum(mem.values()))
