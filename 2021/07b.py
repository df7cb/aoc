#!/usr/bin/python3

with open('07.txt') as f:
    subs = [int(x) for x in f.readline().split(',')]

print(subs)

def fuel(subs, pos):
    f = 0
    for sub in subs:
        d = abs(pos-sub)
        f += (d * (d+1)) // 2
    return f

for pos in range(max(subs)+1):
    print(pos, fuel(subs, pos))
