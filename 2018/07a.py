#!/usr/bin/python3

import re

tasks = {} # task -> set(prerequisites)

with open('07.txt') as f:
    for line in f:
        m = re.match('Step (.) must be finished before step (.) can begin.', line)
        (a, b) = m.groups()
        if a not in tasks:
            tasks[a] = set()
        if b not in tasks:
            tasks[b] = set()
        tasks[b].add(a)

while len(tasks) > 0:
    for t in sorted(tasks):
        if len(tasks[t]) == 0:
            print(t, end='')
            del tasks[t]
            for t2 in tasks:
                tasks[t2].discard(t)
            break

print()
