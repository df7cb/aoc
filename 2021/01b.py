#!/usr/bin/python3

with open('1.txt') as f:
    depths = [x for x in map(int, f.readlines())]

last = None
incs = 0

for i in range(len(depths)-2):
    s = sum(depths[i:i+3])
    if last and s > last:
        incs += 1
    last = s

print("Increments:", incs)
