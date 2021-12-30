#!/usr/bin/python3

import re

constellations = []

with open('25.txt') as f:
    for line in f:
        m = re.match('([\d-]+),([\d-]+),([\d-]+),([\d-]+)', line)
        constellations.append([[int(x) for x in m.groups()]])

print(constellations)

def dist(b1, b2):
    return abs(b1[0]-b2[0]) + abs(b1[1]-b2[1]) + abs(b1[2]-b2[2]) + abs(b1[3]-b2[3])

def try_merge():
    for c1 in range(len(constellations)):
        for c2 in range(c1+1, len(constellations)):
            for p1 in constellations[c1]:
                for p2 in constellations[c2]:
                    if dist(p1, p2) <= 3:
                        print("merge", c1, c2)
                        constellations[c1].extend(constellations[c2])
                        constellations[c2] = []
                        return True
    return False

while(try_merge()):
    print("constellations:", len([x for x in constellations if len(x) > 0]))
    pass
