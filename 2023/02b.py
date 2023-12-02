#!/usr/bin/python3

import re


sum = 0

with open("02.txt") as f:
    for line in f:

        possible = {
                'red': 0,
                'green': 0,
                'blue': 0,
                }

        if m := re.match('Game (\d+): (.*)', line):
            game = int(m.group(1))
            blocks = m.group(2)

            for b in blocks.split('; '):
                for b2 in b.split(', '):
                    num, color = b2.split(' ')
                    if int(num) > possible[color]:
                        possible[color] = int(num)

            this = possible['red'] * possible['green'] * possible['blue']
            print(game, this)
            sum += this

print(sum)
