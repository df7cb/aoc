#!/usr/bin/python3

import re

pair = {}

with open('14.txt') as f:
    polymer = f.readline().strip()
    f.readline()
    for line in f:
        m = re.match('(..) -> (.)', line)
        pair[m.group(1)] = m.group(2)

print(polymer)
print(pair)

def step(polymer):
    polymer2 = []
    for pos in range(len(polymer)-1):
        insert = pair[polymer[pos:pos+2]]
        polymer2.append(polymer[pos])
        polymer2.append(insert)
    polymer2.append(polymer[-1])
    return ''.join(polymer2)

def score(polymer):
    num = {}
    for p in polymer:
        if p not in num:
            num[p] = 0
        num[p] += 1
    mini, maxi = num[p], num[p]
    for p in num:
        if num[p] < mini:
            mini = num[p]
        if num[p] > maxi:
            maxi = num[p]
    return maxi - mini


for i in range(10):
    polymer = step(polymer)
    print(i, len(polymer), score(polymer), polymer)
