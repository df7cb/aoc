#!/usr/bin/python3

import re
from random import randrange

#pos=<-10401751,8998791,-4822601>, r=53367159

nanobots = [] # top point, bottom point

with open('23.txt') as f:
    for line in f:
        m = re.match('pos=<([\d-]+),([\d-]+),([\d-]+)>, r=([\d-]+)', line)
        c = [int(x) for x in m.groups()]
        nanobots.append([c[0]+c[3], c[1], c[2], c[0]-c[3], c[1], c[2]])

print(nanobots)

def dist(b1, b2):
    return abs(b1[0]-b2[0]) + abs(b1[1]-b2[1]) + abs(b1[2]-b2[2])

def in_range(b):
    n = 0
    for bot in nanobots:
        if dist(bot, b) <= bot[3]:
            n += 1
    return n

print(in_range([0, 0, 0]))

best = 0
bestbot = None
x = 0
while True:
    #b = [randrange(mn[0], mx[0]+1), randrange(mn[1], mx[1]+1), randrange(mn[2], mx[2]+1)]
    #b = [randrange(0, mx[0]+1), randrange(0, mx[1]+1), randrange(0, mx[2]+1)]
    b = [randrange(9000000,16000000), randrange(6000000, 10000000), randrange(10000000, 11000000)]
    i = in_range(b)
    if i >= best:
        best = i
        bestbot = b
    x+=1
    if x%100==0:
        print(best, bestbot, i, b)

# 836 [9758195, 6639935, 10262403]
# 837 [15643848, 7435510, 10274496]
# 852 [13231442, 9063597, 11429516]
# 859 [15715315, 9264614, 11677895]
# 859 [13416861, 9948228, 10911874]
# 860 [13081901, 9989946, 10678641]
# 860 [12994919, 9962861, 10612790]
# 860 [13244983, 9998825, 10869392]
# 860 [13066446, 9991902, 10737156]
# 860 [13188088, 9943871, 10878171]

#b = [13188088, 9943871, 10878171]
#while in_range(b) >= 860:
#    print(in_range(b), dist(b, [0, 0, 0]), b)
#    b[0] -= 1000
#
#b[0] += 1000
#print(in_range(b), dist(b, [0, 0, 0]), b)
#
#while in_range(b) >= 860:
#    print(in_range(b), dist(b, [0, 0, 0]), b)
#    b[0] -= 1
#
#b[0] += 1
#print(in_range(b), dist(b, [0, 0, 0]), b)
