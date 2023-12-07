#!/usr/bin/python3

import re

ranks = list("AKQJT98765432")
ranks.reverse()

def shape(hand):
    cards = {}
    for card in hand:
        if card not in cards:
            cards[card] = 1
        else:
            cards[card] += 1

    shp = sorted(cards.values())
    shp.reverse()

    print(f"{hand} shape is {shp}")

    if shp == [5]: return 6
    elif shp == [4,1]: return 5
    elif shp == [3,2]: return 4
    elif shp == [3,1,1]: return 3
    elif shp == [2,2,1]: return 2
    elif shp == [2,1,1,1]: return 1
    elif shp == [1,1,1,1,1]: return 0
    else:
        raise Exception(hand, shp)

def high_card(hand):
    return list([ranks.index(x) for x in hand])

def hand_key(hand):
    key = (shape(hand), high_card(hand))
    print(f"{hand} key is {key}")
    return key

hands = []

with open("07.txt") as f:
    for line in f:
        card, bid = line.split()
        hands.append((card, int(bid)))

print(hands)

hands.sort(key=lambda x: hand_key(x[0]))

print(hands)

win = 0

for i in range(len(hands)):
    win += (i+1) * hands[i][1]

print(win)
