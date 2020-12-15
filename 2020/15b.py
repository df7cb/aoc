#!/usr/bin/python3

puzzle = '2,20,0,4,1,17'.split(',')
#puzzle = '0,3,6'.split(',')

spoken = {}
for x in range(len(puzzle)-1): # don't save last element yet
    spoken[int(puzzle[x])] = int(x)+1
last = int(puzzle[-1])

#print(spoken)

round = len(puzzle)
#while round < 15:
#while round < 2020:
while round < 30000000:
    if round % 100000 == 0:
        print(round, len(spoken))
    if last in spoken:
        next = round - spoken[last]
    else:
        next = 0
    spoken[last] = round
    #print(round, last, next), spoken)

    last = next
    round += 1

print(last)

#print(spoken)
