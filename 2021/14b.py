#!/usr/bin/python3

import re
from collections import defaultdict

pairs = defaultdict(int)
productions = {}

with open('14.txt') as f:
    polymer = f.readline().strip()
    for pos in range(len(polymer)-1):
        pair = polymer[pos:pos+2]
        pairs[pair] += 1

    f.readline()

    for line in f:
        m = re.match('(..) -> (.)', line)
        productions[m.group(1)] = m.group(2)

print(pairs)
print(productions)

def step(polymer):
    pairs2 = defaultdict(int)
    for pair in pairs:
        prod = productions[pair]
        pairs2[pair[0]+prod] += pairs[pair]
        pairs2[prod+pair[1]] += pairs[pair]

    return pairs2

def score(pairs):
    mini, maxi = None, None
    count = defaultdict(int)
    for pair in pairs:
        count[pair[0]] += pairs[pair]
    # account for last character
    count[polymer[-1]] += 1

    for p in count:
        if mini is None:
            mini = count[p]
        if maxi is None:
            maxi = count[p]
        if count[p] < mini:
            mini = count[p]
        if count[p] > maxi:
            maxi = count[p]
    return maxi - mini

for i in range(40):
    pairs = step(pairs)
    print(i, score(pairs), pairs)
