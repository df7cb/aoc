#!/usr/bin/python3

sum = 0

chars = []
for i in range(8):
    chars.append({})

with open('06.txt') as f:
    for line in f:
        for p in range(len(line.strip())):
            char = line[p]
            if char not in chars[p]:
                chars[p][char] = 0
            chars[p][char] += 1

for char in chars:
    m = max(char.values())
    print(''.join([x for x in char if char[x] == m]), end='')

print()
