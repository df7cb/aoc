#!/usr/bin/python3

import re

contains = {}
contained = {}

with open('7.txt') as f:
    for rule in f:
        m = re.match('(.*) bags contain (.*)', rule)
        outer_color = m.group(1)
        if outer_color not in contained:
            contained[outer_color] = []
        if m.group(2) == 'no other bags.':
            #print (outer_color, m.group(2))
            contains[outer_color] = []
            continue

        inners = re.findall('\d+ ([^,]*) bag', m.group(2))
        contains[outer_color] = inners
        #print(outer_color, 'contains', inners)
        for i in inners:
            #print(f"{outer_color}\t{i}")
            if i not in contained:
                contained[i] = []
            if i not in contains:
                contains[i] = []
            #print(outer_color, 'contains', i)
            contained[i].append(outer_color)

#print(contained)

outers = []

def find(color):
    #print('looking at', color)
    if color in outers:
        return
    outers.append(color)
    for c in contained[color]:
        find(c)

find('shiny gold')

print(len(outers) - 1, outers)
