#!/usr/bin/python3

with open('6.txt') as f:
    groups = f.read().split("\n\n")

print(groups)

count = 0

for group in groups:
    persons = group.split()
    print(persons)
    for question in range(26):
        char = chr(97+question)
        for person in persons:
            if char not in person:
                break
        else:
            count += 1

print(count)
