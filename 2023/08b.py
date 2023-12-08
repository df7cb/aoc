#!/usr/bin/python3

import re

instr = {}
where = []

with open("08.txt") as f:
    dirs = f.readline().strip()
    f.readline()

    for line in f:
        m = re.match('(.*) = \((.*), (.*)\)', line)
        instr[m.group(1)] = (m.group(2), m.group(3))
        if m.group(1)[-1] == 'A':
            where.append(m.group(1))

#print(dirs)
#print(instr)

count = 0

while True:
    for d in dirs:
        finished = True
        for w in range(len(where)):
            if d == 'L':
                where[w] = instr[where[w]][0]
            else:
                where[w] = instr[where[w]][1]
            if where[w][-1] != 'Z':
                finished = False
        count += 1

        if finished:
            print(count, where)
            exit()

    #if count % 10000 == 0:
    print(count, where)

