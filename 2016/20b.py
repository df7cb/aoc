#!/usr/bin/python3

import re

last_ip = 2**32 - 1

ranges = []

with open('20.txt') as f:
    for line in f:
        m = re.match('(\d+)-(\d+)', line)
        ranges.append((int(m[1]), int(m[2])))

ranges.sort(key = lambda x: x[0])
#print(ranges)

ranges2 = [ranges[0]]
for a, b in ranges:
    a0, b0 = ranges2[-1]
    if a <= b0 + 1:
        ranges2[-1] = (a0, max(b, b0))
    else:
        ranges2.append((a, b))

#print(ranges2)

free = 0
for p in range(len(ranges2)-1):
    assert ranges2[p+1][0] > ranges2[p][1] + 1
    free1 = ranges2[p+1][0] - ranges2[p][1] - 1
    print(ranges2[p], free1, ranges2[p+1])
    free += free1

if ranges2[-1][1] <= last_ip:
    free1 = last_ip - ranges2[-1][1]
    print(ranges2[-1], free1, last_ip)
    free += free1

print('20b:', free)
