#!/usr/bin/python3

xmas = []

with open('09.txt') as f:
    for line in f:
        xmas.append(int(line))

for p1 in range(len(xmas)):
    for p2 in range(p1+1, len(xmas)):
        if sum(xmas[p1:p2]) == 21806024:
            print(p1, p2, xmas[p1:p2], min(xmas[p1:p2]) + max(xmas[p1:p2]))
