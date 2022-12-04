#!/usr/bin/python3

total = 0

with open("03.txt") as f:
    for line in f:
        line = line.strip()

        left = set(line[:len(line)//2])
        for item in line[len(line)//2:]:
            if item in left:
                val = ord(item) - 96 if ord(item) >= 96 else 26 + ord(item) - 64
                total += val
                print(line, left, item, val)
                break

print(total)
