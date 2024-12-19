#!/usr/bin/python3

import re

ok = 0
num = 0

cache = {}

def check(s, towels):
    if s in cache: return cache[s]
    if s == '': return 1
    r = 0
    for t in towels:
        l = len(t)
        if s[:l] == t:
            r += check(s[l:], towels)
    cache[s] = r
    return r

with open("19.txt") as f:
    towels = f.readline().strip().split(', ')
    print(towels)
    f.readline()

    for line in f:
        line = line.strip()
        r = check(line, towels)
        print(line, r)
        if r > 0:
            ok += 1
        num += r

print(ok)
print(num)
