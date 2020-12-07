#!/usr/bin/python3

import re

contains = {}

with open('7.txt') as f:
    for rule in f:
        m = re.match('(.*) bags contain (.*)', rule)
        outer_color = m.group(1)
        if m.group(2) == 'no other bags.':
            #print (outer_color, m.group(2))
            contains[outer_color] = []
            continue

        inners = re.findall('(\d+) ([^,]*) bag', m.group(2))
        contains[outer_color] = inners
        #print(outer_color, 'contains', inners)
        for i in inners:
            #print(f"{outer_color}\t{i}")
            if i not in contains:
                contains[i] = []
            #print(outer_color, 'contains', i)

def find(color):
    bags = 0
    for number, inner_color in contains[color]:
        inner_number = find(inner_color)
        print(color, 'contains', number, inner_color, inner_number)
        bags += int(number) * inner_number
    return 1 + bags

print(find('shiny gold') - 1)
