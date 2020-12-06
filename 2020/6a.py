#!/usr/bin/python3

with open('6.txt') as f:
    groups = f.read().split("\n\n")

print(groups)

count = 0

for group in groups:
    for question in range(26):
        char = chr(97+question)
        if char in group:
            count += 1

print(count)
