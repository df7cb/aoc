#!/usr/bin/python3

with open("08.txt") as f:
    forest = [x.strip() for x in f]

visible = 0
for y in range(len(forest)):
    for x in range(len(forest[0])):
        tree = forest[y][x]
        if x == 0 or tree > max(forest[y][:x]):
            visible += 1
        elif x == len(forest[0]) - 1 or tree > max(forest[y][x+1:]):
            visible += 1
        elif y == 0 or tree > max([row[x] for row in forest[:y]]):
            visible += 1
        elif y == len(forest) - 1 or tree > max([row[x] for row in forest[y+1:]]):
            visible += 1

print(visible)

