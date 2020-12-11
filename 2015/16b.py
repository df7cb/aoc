#!/usr/bin/python3

import re

present = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
}

with open('16.txt') as f:
    for line in f:
        m = re.match('Sue ([^:]*): (.*)', line)
        for things in re.findall('([^ ,:]*): (\d+)', m[2]):
            if things[0] in ('cats', 'trees'):
                if present[things[0]] >= int(things[1]):
                    break
            elif things[0] in ('pomeranians', 'goldfish'):
                if present[things[0]] <= int(things[1]):
                    break
            else:
                if present[things[0]] != int(things[1]):
                    break
        else:
            print(line)
