#!/usr/bin/python3

import re

mem = {}

def write(mask, address, value):
    if 'X' in mask:
        thisbit0 = int(mask.replace('0', '1').replace('X', '0', 1).replace('X', '1'), 2)
        thisbit1 = int(mask.replace('1', '0').replace('X', '1', 1).replace('X', '0'), 2)
        write(mask.replace('X', '0', 1), address & thisbit0, value)
        write(mask.replace('X', '1', 1), address | thisbit1, value)
    else:
        mem[address] = value

with open('14.txt') as f:
    for line in f:
        if m := re.match('mask = (.+)', line):
            mask = m[1]
            ones = int(m[1].replace('X', '0'), 2)
        elif m := re.match('mem\[(\d+)\] = (\d+)', line):
            write(mask, int(m[1]) | ones, int(m[2]))

for i in mem:
    print(i, mem[i])

print(sum(mem.values()))
