#!/usr/bin/python3

total = 0

with open("03.txt") as f:
    bags = [l.strip() for l in f.readlines()]

for g in range(0, len(bags), 3):
    items = set(bags[g]).intersection(set(bags[g+1]), set(bags[g+2]))

    for item in items: # only one in there anyway
        print(item)
        val = ord(item) - 96 if ord(item) >= 96 else 26 + ord(item) - 64
        total += val

print(total)
