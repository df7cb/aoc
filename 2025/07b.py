#!/usr/bin/python3

with open("07.txt") as f:
    splitter = [list(line.strip()) for line in f.readlines()]

cache = {}

def walk(i, j):
    if (i, j) in cache: return cache[(i, j)]
    if i == len(splitter) - 1:
        return 1
    if splitter[i][j] in ('.', 'S'):
        return walk(i+1, j)
    if splitter[i][j] == '^':
        cache[(i, j)] = walk(i+1, j-1) + walk(i+1, j+1)
        return cache[(i, j)]

j = splitter[0].index('S')
print(walk(0, j))
