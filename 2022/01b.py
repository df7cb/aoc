#!/usr/bin/python3

elves = []

with open("01.txt") as f:
    group = 0
    maxgroup = 0

    for line in f:
        if line == "\n":
            elves.append(group)
            group = 0
        else:
            group += int(line)

elves.append(group)

elves.sort()

print(elves[-3] + elves[-2] + elves[-1])
