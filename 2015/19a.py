#!/usr/bin/python3

from copy import deepcopy
import re

element = {}

def expand(string):
    return re.findall('[A-Z][a-z]*', string)

with open('19.txt') as f:
    for line in f:
        if m := re.match('(.*) => (.*)', line):
            if m[1] not in element:
                element[m[1]] = []
            element[m[1]].append(expand(m[2]))

        else:
            data = expand(line)

print(data)

found = {}

for p in range(len(data)):
    if data[p] not in element:
        continue
    for el in element[data[p]]:
        data2 = deepcopy(data)
        data2[p:p+1] = el
        data3 = "".join(data2)
        print(data3)
        found[data3] = True

print(len(found))
