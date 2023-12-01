#!/usr/bin/python3

sum = 0

with open("01.txt") as f:
    for line in f:
        first = None
        last = None
        for char in line:
            if char in "0123456789":
                if first is None:
                    first = char
                last = char
        sum += int(first + last)
        print(f"{line.strip()} {first} {last}")

print(sum)
