#!/usr/bin/python3

def hash(s):
    val = 0
    for c in s:
        val = ((val + ord(c)) * 17) % 256
    return val

total = 0

with open("15.txt") as f:
    for s in f.readline().strip().split(','):
        h = hash(s)
        print(s, h)
        total += h

print(total)
