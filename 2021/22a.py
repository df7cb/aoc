#!/usr/bin/python3

import re

init = []

with open('22.txt') as f:
    # on x=-16..31,y=1..46,z=-4..43
    for line in f:
        m = re.match('(on|off) x=([\d-]+)..([\d-]+),y=([\d-]+)..([\d-]+),z=([\d-]+)..([\d-]+)', line)
        init.append([m.group(1)=='on'] + [int(x) for x in m.groups()[1:]])

print(init)

cubes=set()

for i in init:
    if i[2] < -50 or i[1] > 50 or i[4] < -50 or i[3] > 50 or i[6] < -50 or i[5] > 50:
        continue

    for x in range(i[1], i[2]+1):
        for y in range(i[3], i[4]+1):
            for z in range(i[5], i[6]+1):
                if i[0]:
                    cubes.add((x, y, z))
                else:
                    cubes.discard((x, y, z))

print(len(cubes))
