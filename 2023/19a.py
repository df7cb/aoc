#!/usr/bin/python3

import re

workflow = {}

accept = []

def handle(part):
    print(part)

    queue = 'in'
    while True:
        if queue == 'A':
            accept.append(part)
            return
        elif queue == 'R':
            return

        for rule in workflow[queue]:
            if m := re.match('(\w)<(\d+):(\w+)', rule):
                if part[m.group(1)] < int(m.group(2)):
                    queue = m.group(3)
                    break
            elif m := re.match('(\w)>(\d+):(\w+)', rule):
                if part[m.group(1)] > int(m.group(2)):
                    queue = m.group(3)
                    break
            else:
                queue = rule
                break

with open("19.txt") as f:
    for line in f:
        if line == "\n": break
        m = re.match('(\w+)\{(.*)\}', line)
        workflow[m.group(1)] = m.group(2).split(',')

    for line in f:
        m = re.match('\{x=(.*),m=(.*),a=(.*),s=(.*)\}', line)
        handle({'x': int(m.group(1)), 'm': int(m.group(2)), 'a': int(m.group(3)), 's': int(m.group(4))})

total = 0

#print(accept)
for part in accept:
    s = sum(part.values())
    print(part, s)
    total += s

print(total)
