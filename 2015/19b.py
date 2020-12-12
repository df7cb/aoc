#!/usr/bin/python3

import re
import random

origin = {}
molecules = []

with open('19.txt') as f:
    for line in f:
        if m := re.match('(.*) => (.*)', line):
            origin[m[2]] = m[1]
            molecules.append(m[2])

        else:
            data = line.strip()

count = 0
while data != 'e':
    o = random.choice(molecules)
    if o in data:
        data = data.replace(o, origin[o], 1)
        count += 1
        print(o, data)
print(count)
