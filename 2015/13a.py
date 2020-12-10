#!/usr/bin/python3

import re
from itertools import permutations

neighbor = {}

with open('13.txt') as f:
    for line in f:
        m = re.match('(.*) would (gain|lose) (\d+) happiness units by sitting next to (.*).', line)
        happy = int(m[3])
        if m[2] == 'lose':
            happy *= -1
        if m[1] not in neighbor:
            neighbor[m[1]] = {}
        neighbor[m[1]][m[4]] = happy

best = 0

for perm in permutations(neighbor.keys()):
    if perm[0] != 'Alice':
        continue
    happy = 0
    for p in range(len(perm)):
        p2 = p+1
        if p2 == len(perm):
            p2 = 0
        happy += neighbor[perm[p]][perm[p2]]
        happy += neighbor[perm[p2]][perm[p]]
    if happy >= best:
        print(happy, perm)
        best = happy
