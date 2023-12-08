#!/usr/bin/python3

import re

instr = {}

with open("08.txt") as f:
    dirs = f.readline().strip()
    f.readline()

    for line in f:
        m = re.match('(.*) = \((.*), (.*)\)', line)
        instr[m.group(1)] = (m.group(2), m.group(3))

print(dirs)
print(instr)

where = 'AAA'
count = 0

while where != 'ZZZ':
    for d in dirs:
        if d == 'L':
            where = instr[where][0]
        else:
            where = instr[where][1]
        count += 1
        print(count, where)
        if where == 'ZZZ':
            break

print(count)
