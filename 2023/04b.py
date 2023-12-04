#!/usr/bin/python3

import re

cards = []

with open("04.txt") as f:
    for line in f:
        m = re.match('Card *(\d+): (.*) \| (.*)', line)
        a = set(m.group(2).split())
        b = set(m.group(3).split())
        c = a.intersection(b)

        cards.append({"n": m.group(1), "c": len(c), "num": 1})

for card in range(len(cards)):
    print(cards[card])
    for i in range(cards[card]["c"]):
        if card + i + 1>= len(cards):
            continue
        cards[card + i + 1]["num"] += cards[card]["num"]
        print(" ", cards[card + i + 1])

print(sum([ card["num"] for card in cards ]))
