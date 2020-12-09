#!/usr/bin/python3

import re

nodes = {}
dist = {}

with open('9.txt') as f:
    for line in f:
        m = re.match('(.*) to (.*) = (\d+)', line)
        nodes[m[1]] = True
        nodes[m[2]] = True
        dist[m[1], m[2]] = int(m[3])
        dist[m[2], m[1]] = int(m[3])

maxdist = 10000

def walk(path, d):
    #print(path, d)
    if len(path) == len(nodes):
        global maxdist
        if d <= maxdist:
            print(path, d)
            maxdist = d
        #if d == 95:
        #    exit(0)
        return

    for nextnode in nodes:
        if nextnode in path:
            continue
        if path == []:
            walk([nextnode], 0)
        else:
            walk(path + [nextnode], d + dist[path[-1], nextnode])

walk([], 0)
