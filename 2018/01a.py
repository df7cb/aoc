#!/usr/bin/python3

freq = 0

with open("01.txt") as f:
    for line in f:
        freq += int(line)

print(freq)
