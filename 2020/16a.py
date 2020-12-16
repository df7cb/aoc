#!/usr/bin/python3

import re

valid_numbers = set()
error_rate = 0
valid_tickets = []

with open('16.txt') as f:
    for line in f:
        if m := re.match('(.*): (\d+)-(\d+) or (\d+)-(\d+)', line):
            for x in list(range(int(m[2]), int(m[3])+1)) + list(range(int(m[4]), int(m[5])+1)):
                valid_numbers.add(x)

        elif ',' in line:
            for i in [int(x) for x in line.split(',')]:
                if i not in valid_numbers:
                    error_rate += i
                    break
            else:
                valid_tickets.append([int(x) for x in line.split(',')])

print(error_rate)
#print(valid_tickets)
