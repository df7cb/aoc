#!/usr/bin/python3

import re

with open('09.txt') as f:
    data = f.read()

output = ''
p = 0
while p < len(data.strip()):
    if m := re.match('\((\d+)x(\d+)\)', data[p:]):
        length, repeat = int(m[1]), int(m[2])
        p += len(m[0])
        output += data[p:p+length] * repeat
        p += length
    else:
        output += data[p]
        p += 1

print(output)
print(len(output))
