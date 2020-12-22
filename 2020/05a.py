#!/usr/bin/python3

max = -1

with open('05.txt') as f:
    for line in f:
        binary = line.replace('F', '0').replace('B', '1').replace('R', '1').replace('L', '0').strip()
        number = int(binary, 2)
        if number > max:
            max = number

print(max)
