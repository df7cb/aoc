#!/usr/bin/python3

puzzle = '2,20,0,4,1,17'
#puzzle = '0,3,6'

spoken = [int(x) for x in puzzle.split(',')]
spoken.reverse()

print(spoken)

while len(spoken) < 2020:
    now = spoken[0]
    if now in spoken[1:]:
        last = spoken.index(now, 1)
        spoken.insert(0, last)
    else:
        spoken.insert(0, 0)

print(spoken)
