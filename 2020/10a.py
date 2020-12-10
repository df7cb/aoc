#!/usr/bin/python3

adapters = [0] # outlet

with open('10.txt') as f:
    for line in f:
        adapters.append(int(line))

adapters.sort()

adapters.append(adapters[len(adapters)-1] + 3) # my device

print(adapters)

j1 = 0
j3 = 0

for p in range(len(adapters)-1):
    if adapters[p+1] - adapters[p] == 1:
        j1 += 1
    if adapters[p+1] - adapters[p] == 3:
        j3 += 1

print (j1, j3, j1*j3)
