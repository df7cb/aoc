#!/usr/bin/python3

import re

maps = {}

with open("05.txt") as f:
    m = re.match('seeds: (.*)', f.readline())
    seeds = [int(x) for x in m.group(1).split()]
    seeds = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]
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

#print(maps)

while have != "location":
    print("have", have, seeds)
    mapp = maps[have]

    seeds2 = []
    while len(seeds) > 0:
        seed = seeds.pop()
        assert seed[1] > 0

        translated = False
        for conv in mapp["convs"]:
            #print ("checking", seed, conv)
            if seed[0] + seed[1] <= conv[1] or seed[0] >= conv[1] + conv[2]: # no overlap
                pass
                #print(seed, conv, "no overlap")
            else:
                if seed[0] < conv[1]: # left overhang
                    seeds.append((seed[0], conv[1] - seed[0])) # feed back left part into processing
                    seed = (conv[1], seed[1] - (conv[1] - seed[0])) # remaining part
                    #print("left overhang", seeds[-1], seed)
                if seed[0] + seed[1] > conv[1] + conv[2]: # right overhang
                    seeds.append((conv[1] + conv[2], seed[0] + seed[1] - (conv[1] + conv[2])))
                    seed = (seed[0], seed[1] - (seed[0] + seed[1] - (conv[1] + conv[2])))
                    #print("left overhang", seeds[-1], seed)
                translated = True
                seeds2.append((seed[0] + conv[0] - conv[1], seed[1]))
                #print("translated", seeds2[-1])

        if not translated:
            seeds2.append(seed)
            #print("not translated", seeds2[-1])

    seeds = seeds2

    have = mapp["to"]

print("lowest:", min(seeds))
