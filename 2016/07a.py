#!/usr/bin/python3

import re

good = 0

with open('07.txt') as f:
    for line in f:
        r = re.compile('[^\[\]]*(\[(?![^\[\]]*(?P<a0>\w)(?!(?P=a0))(?P<b0>\w)(?P=b0)(?P=a0))[^\[\]]*\][^\[\]]*)*((?P<a>\w)(?!(?P=a))(?P<b>\w)(?P=b)(?P=a))[^\[\]]*(\[(?![^\[\]]*(?P<a1>\w)(?!(?P=a1))(?P<b1>\w)(?P=b1)(?P=a1))[^\[\]]*\][^\[\]]*)*')
        if m := r.fullmatch(line.strip()):
            print(line.strip(), m[2])
            good += 1

print(good)
