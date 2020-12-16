#!/usr/bin/python3

import re

good = 0

with open('07.txt') as f:
    for line in f:
        r = re.compile("""
                ((?P<a>\w)(?!(?P=a))(?P<b>\w)(?P=a)) # ABA, outside
                [^\[\]]*(\[[^\[\]]*\][^\[\]]*)*      # any number of [] pairs
                \[[^\[\]]*(?P=b)(?P=a)(?P=b)         # opening [ and BAB
                |
                ((?P<c>\w)(?!(?P=c))(?P<d>\w)(?P=c)) # ABA, inside
                [^\[\]]*\]                           # closing ]
                [^\[\]]*(\[[^\[\]]*\][^\[\]]*)*      # any number of [] pairs
                (?P=d)(?P=c)(?P=d)                   # BAB
                """, re.X)
        if m := r.search(line.strip()):
            print(line.strip(), m[1])
            good += 1

print(good)
