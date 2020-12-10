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
    people = ['Me'] + list(perm)
    happy = 0
    for p in range(len(people)):
        p2 = p+1
        if p2 == len(people):
            p2 = 0
        if p != 0 and p2 != 0:
            happy += neighbor[people[p]][people[p2]]
            happy += neighbor[people[p2]][people[p]]
    if happy >= best:
        print(happy, people)
        best = happy
