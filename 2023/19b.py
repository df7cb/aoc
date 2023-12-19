#!/usr/bin/python3

import re
from copy import deepcopy

workflow = {}

accept = []

def handle(part, queue, depth):
    print("  "*depth, part, queue)

    if queue == 'A':
        accept.append(part)
        return
    elif queue == 'R':
        return

    for rule in workflow[queue]:
        print("  "*depth, part, rule)
        if m := re.match('(\w)([<>])(\d+):(\w+)', rule):
            key = m.group(1)
            op = m.group(2)
            val = int(m.group(3))
            que = m.group(4)
            l, u = part[key]

            if op == '<':
                if l < val:
                    # make a new part with the lower half
                    partl = deepcopy(part)
                    partl[key][1] = min(u, val - 1)
                    print("  "*depth, "new part", partl)
                    handle(partl, que, depth+1)
                # continue with upper half in this loop
                part[key][0] = max(l, val)
                print("  "*depth, "old part", part)
                if part[key][0] > part[key][1]:
                    print("  "*depth, "old part is empty", part)
                    return

            if op == '>':
                if u > val:
                    # make a new part with the upper half
                    partl = deepcopy(part)
                    partl[key][0] = max(l, val + 1)
                    print("  "*depth, "new part", partl)
                    handle(partl, que, depth+1)
                # continue with lower half in this loop
                part[key][1] = min(u, val)
                print("  "*depth, "old part", part)
                if part[key][0] > part[key][1]:
                    print("  "*depth, "old part is empty", part)
                    return

        else:
            handle(part, rule, depth+1)

with open("19.txt") as f:
    for line in f:
        if line == "\n": break
        m = re.match('(\w+)\{(.*)\}', line)
        workflow[m.group(1)] = m.group(2).split(',')

handle({'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]}, 'in', 0)

print()
total = 0

#print(accept)
for part in accept:
    n = 1
    for key in part:
        assert part[key][1] > part[key][0]
        n *= part[key][1] - part[key][0] + 1
    print(part, n)
    total += n

print(total)
