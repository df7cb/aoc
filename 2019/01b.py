#!/usr/bin/python3

def fuel(mass):
    if mass <= 0:
        return 0
    f = max(mass//3 - 2, 0)
    return f + fuel(f)

with open("01.txt") as f:
    print(sum([fuel(int(x)) for x in f]))
