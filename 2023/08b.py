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

count = 0

finish = [0 for x in where]

while True:
    for d in dirs:
        count += 1
        finished = True
        for w in range(len(where)):
            if d == 'L':
                where[w] = instr[where[w]][0]
            else:
                where[w] = instr[where[w]][1]
            if where[w][-1] != 'Z':
                finished = False
            else:
                print("finish", w, count - finish[w], count)
                finish[w] = count

        if finished:
            print(count, where)
            exit()

    for w in range(len(where)):
        if where[w][-1] == 'Z':
            print(w, "finished at end", count)
    #if count % 10000 == 0:
    #    print(count, where)

#... manually solved after reading the output :)
