#!/usr/bin/python3

import re

finish = 2503
deers = {}

with open('14.txt') as f:
    for line in f:
        m = re.match('(.*) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.', line)
        deers[m[1]] = {"speed": int(m[2]), "duration": int(m[3]), "rest": int(m[4]), "pos": 0, "points": 0}

for tick in range(finish):
    bestpos, bestdeer = 0, None
    for d in deers:
        deer = deers[d]
        if tick % (deer['duration'] + deer['rest']) < deer['duration']:
            deer['pos'] += deer['speed']
        if deer['pos'] > bestpos:
            bestpos = deer['pos']
            bestdeer = d
    deers[bestdeer]['points'] += 1

for d in deers:
    print(d, deers[d])
