#!/usr/bin/python3

import re

ingredient = {}

with open('15.txt') as f:
    for line in f:
        m = re.match('(.*): capacity (.*), durability (.*), flavor (.*), texture (.*), calories (.*)', line)

        ingredient[m[1]] = {
                "capacity": int(m[2]),
                "durability": int(m[3]),
                "flavor": int(m[4]),
                "texture": int(m[5]),
                "calories": int(m[6])}

best = 0

for spr in range(0, 101):
    for but in range(0, 101 - spr):
        for cho in range(0, 101 - spr - but):
            can = 100 - spr - but - cho
            total = 1
            cal = ingredient['Sprinkles']['calories'] * spr + \
                  ingredient['Butterscotch']['calories'] * but + \
                  ingredient['Chocolate']['calories'] * cho + \
                  ingredient['Candy']['calories'] * can
            if cal != 500:
                continue
            for typ in ['capacity', 'durability', 'flavor', 'texture']:
                summ = ingredient['Sprinkles'][typ] * spr + \
                       ingredient['Butterscotch'][typ] * but + \
                       ingredient['Chocolate'][typ] * cho + \
                       ingredient['Candy'][typ] * can
                if summ < 0:
                    total = 0
                else:
                    total *= summ
            if total > best:
                print(spr, but, cho, can, cal, total)
                best = total
