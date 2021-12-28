#!/usr/bin/python3

import re

#pos=<-10401751,8998791,-4822601>, r=53367159

nanobots = []

with open('23.txt') as f:
    for line in f:
        m = re.match('pos=<([\d-]+),([\d-]+),([\d-]+)>, r=([\d-]+)', line)
        nanobots.append([int(x) for x in m.groups()])

mx = 0
for bot in nanobots:
    if bot[3] > mx:
        mx = bot[3]
        mxbot = bot

def dist(b1, b2):
    return abs(b1[0]-b2[0]) + abs(b1[1]-b2[1]) + abs(b1[2]-b2[2])

print(mxbot)

bots = 0
for bot in nanobots:
    if dist(bot, mxbot) <= mx:
        bots += 1

print(bots)
