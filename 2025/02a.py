#!/usr/bin/python3

count = 0

with open("02.txt") as f:
    line = f.read().strip()
    for rng in line.split(','):
        l, r = rng.split('-')
        print(l, r)
        li, ri = int(l), int(r)
        for i in range(li, ri + 1):
            t = str(i)
            le = len(t) // 2
            if t[:le] == t[le:]:
                print(t)
                count += i

print(count)
