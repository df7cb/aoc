#!/usr/bin/python3

with open('1.txt') as f:
    last = None
    incs = 0
    for l in f:
        i = int(l)
        if last and i > last:
            incs += 1
        last = i

print("Increments:", incs)
