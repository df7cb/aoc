#!/usr/bin/python3

with open("01.txt") as f:
    group = 0
    maxgroup = 0

    for line in f:
        if line == "\n":
            print(group)
            if group > maxgroup:
                maxgroup = group
            group = 0
        else:
            group += int(line)


if group > maxgroup:
    maxgroup = group

print(maxgroup)
