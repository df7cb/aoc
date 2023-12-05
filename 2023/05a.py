#!/usr/bin/python3

import re

maps = {}

with open("05.txt") as f:
    m = re.match('seeds: (.*)', f.readline())
    seeds = [int(x) for x in m.group(1).split()]
    have = "seed"
    print(seeds)

    f.readline()

    for line in f:
        m = re.match('(.*)-to-(.*) map:', line)
        maps[m.group(1)] = {"to": m.group(2), "convs": []}
        for line in f:
            if line.strip() == '': break
            conv = [int(x) for x in line.split()]
            maps[m.group(1)]["convs"].append(conv)

print(maps)

while have != "location":
    print("have", have, seeds)
    mapp = maps[have]
    for i in range(len(seeds)):
        seed = seeds[i]
        for conv in mapp["convs"]:
            if conv[1] <= seed < conv[1] + conv[2]:
                seeds[i] = seed + conv[0] - conv[1]
                break
    have = mapp["to"]

print("lowest:", min(seeds))
