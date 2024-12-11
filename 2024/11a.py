#!/usr/bin/python3

with open("11.txt") as f:
    stones = [int(x) for x in f.read().split()]

print(stones)

def step(stones):
    new = []
    for x in stones:
        if x == 0:
            new.append(1)
        elif len(str(x)) % 2 == 0:
            s = str(x)
            l = len(s)
            new.append(int(s[:int(l/2)]))
            new.append(int(s[int(l/2):]))
        else:
            new.append(x * 2024)
    return new

for i in range(25):
    stones = step(stones)
    print(stones)

print(len(stones))
