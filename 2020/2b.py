#!/usr/bin/python3

import re

answer = 0

with open('2.txt') as f:
    for line in f:
        r = re.match('(\d+)-(\d+) (.): (.*)', line)
        if not r:
            raise('huh')
        p1, p2 = int(r.group(1)), int(r.group(2))
        c = r.group(3)
        pw = r.group(4)

        if (pw[p1-1] == c) + (pw[p2-1] == c) == 1:
            print (p1, p2, c, pw)
            answer += 1

print('answer is', answer)
