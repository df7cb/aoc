#!/usr/bin/python3

import re

possible = {
        'red': 12,
        'green': 13,
        'blue': 14,
        }

sum = 0

with open("02.txt") as f:
    for line in f:
        if m := re.match('Game (\d+): (.*)', line):
            game = int(m.group(1))
            blocks = m.group(2)

            for b in blocks.split('; '):
                for b2 in b.split(', '):
                    num, color = b2.split(' ')
                    if int(num) > possible[color]:
                        game = 0

            sum += game

print(sum)
