#!/usr/bin/python3

import re

with open('05.txt') as f:
    polymer = list(f.read().strip())


def reduce(polymer):
    found = True
    while found:
        found = False
        for p in range(len(polymer)-1, 0, -1):
            if p >= len(polymer): continue
            if polymer[p-1] != polymer[p] and polymer[p-1].lower() == polymer[p].lower():
                #print('deleting', p, polymer[p-1], polymer[p])
                polymer[p-1:p+1] = []
                found = True
    return(len(polymer))

for c in range(1, 27):
    char = chr(96+c)
    p = [x for x in polymer if x.lower() != char]
    l = reduce(p)
    print(char, l)
