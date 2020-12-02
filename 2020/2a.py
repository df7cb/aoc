#!/usr/bin/python3

import re

answer = 0

with open('2.txt') as f:
    for line in f:
        r = re.match('(\d+)-(\d+) (.): (.*)', line)
        if not r:
            raise('huh')
        l, h = int(r.group(1)), int(r.group(2))
        c = r.group(3)
        pw = r.group(4)

        matches = filter(lambda x: x == c, pw)
        number = sum(1 for x in matches)

        if l <= number <= h:
            print (l, h, c, pw, number)
            answer += 1

print('answer is', answer)
