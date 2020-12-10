#!/usr/bin/python3

adapters = [0] # outlet

with open('10.txt') as f:
    for line in f:
        adapters.append(int(line))

adapters.sort()

adapters.append(adapters[len(adapters)-1] + 3) # my device

print(adapters)

def count(adapters, p):
    print(adapters)
    if len(adapters) == 1:
        return 1
    if p == len(adapters) - 1:
        return 1
    c = 0
    r = min(p+4, len(adapters))
    for i in range(p+1, r):
        if adapters[i] <= adapters[p] + 3:
            c += count(adapters, i)
    return c

total_count = 1
p0 = 0
for p in range(len(adapters)-1):
    if adapters[p] == adapters[p+1] - 3: # split here
        c = count(adapters[p0:p+1], 0)
        print(adapters[p0:p+1], c)
        total_count *= c
        p0 = p+1

print (total_count)
