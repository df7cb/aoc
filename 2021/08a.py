#!/usr/bin/python3

import re

number_1478 = 0

with open('08.txt') as f:
    for line in f:
        m = re.match('(.*) \| (.*)', line)
        outputs = m.group(2).split(' ')
        print(outputs)

        number_1478 += len([x for x in outputs if len(x) in (2,3,4,7)])

print(number_1478)
