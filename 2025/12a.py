#!/usr/bin/python3

import re

area = {}
fits = 0

with open("12.txt") as f:
    n = None
    for line in f:
        if line == "\n":
            n = None
            continue
        if re.match(r"^(\d):", line):
            n = int(line[0])
            area[n] = 0
        elif n != None:
            if line[0] == '#': area[n] += 1
            if line[1] == '#': area[n] += 1
            if line[2] == '#': area[n] += 1
            print(area)
        elif m := re.match("(\d+)x(\d+): (.*)", line):
            a = int(m.group(1)) * int(m.group(2))
            t = m.group(3).split()
            at = 0
            for i in range(len(t)):
                at += int(t[i]) * area[i]
            print(line.strip(), a, at)
            if at <= a:
                fits += 1

print(fits)
