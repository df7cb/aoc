#!/usr/bin/python3

xmas = []

with open('09.txt') as f:
    for line in f:
        xmas.append(int(line))

for p in range(25, len(xmas)):
    found = False
    for p1 in range(p-25, p):
        for p2 in range(p1+1, p):
            #print(f"{p}: {xmas[p1]} + {xmas[p2]} == {xmas[p1] + xmas[p2]} {xmas[p]}")
            if xmas[p1] + xmas[p2] == xmas[p]:
                print(f"{p}: {xmas[p1]} + {xmas[p2]} == {xmas[p]}")
                found = True
                break
    if not found:
        print('baaaad', p, xmas[p])
