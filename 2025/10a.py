#!/usr/bin/python3

import re
from collections import deque

target = []
buttons = []
joltage = []

with open("10.txt") as f:
    for line in f:
        m = re.match(r"\[(.*)\]", line)
        target.append(tuple([x == '#' for x in m.group(1)]))

        buttons.append([])
        for m in re.findall(r"(?<=\()([\d,]+)(?=\))", line):
            buttons[-1].append(tuple([int(x) for x in m.split(',')]))

        m = re.search(r"\{([\d,]+)\}", line)
        joltage.append(tuple([int(x) for x in m.group(1).split(',')]))

print(target)
print(buttons)
print(joltage)

total = 0

for i in range(len(target)):
    print(target[i])
    start = tuple([False for x in target[i]])
    q = deque([(0, start)])
    while True:
        d, x = q.popleft()
        if x == target[i]: break
        for b in buttons[i]:
            x2 = list(x)
            for bb in b:
                x2[bb] = not x2[bb]
            #print(d+1, x2)
            q.append((d+1, tuple(x2)))
    print(i, d)
    total += d

print(total)
