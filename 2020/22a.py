#!/usr/bin/python3

import re

p = { 1: [], 2: [] }

with open('22.txt') as f:
    for line in f:
        if m := re.match('Player (.*):', line):
            name = int(m[1])
        elif line == "\n":
            pass
        else:
            p[name].insert(0, int(line))

def play(p1, p2):
    top1 = p1.pop()
    top2 = p2.pop()

    if top1 > top2:
        p1.insert(0, top1)
        p1.insert(0, top2)
    else:
        p2.insert(0, top2)
        p2.insert(0, top1)

while len(p[1]) > 0 and len(p[2]) > 0:
    print(p[1], p[2])
    play(p[1], p[2])

def score(p):
    return sum([p[i] * (i+1) for i in range(len(p))])

print("Player 1", score(p[1]))
print("Player 2", score(p[2]))
