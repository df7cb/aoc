#!/usr/bin/python3

import re

p = { 1: [], 2: [] }

with open('22.txt') as f:
    for line in f:
        if m := re.match('Player (.*):', line):
            name = int(m[1])
        elif line == "\n":
            pass
        else:
            p[name].insert(0, int(line))

def game(p1, p2):
    print('=== Game ===')
    print()
    seen = { 1: set(), 2: set() }
    round = 0

    while len(p1) > 0 and len(p2) > 0:
        round += 1
        print('-- Round', round, '--')
        print('Player 1\'s deck:', p1[::-1])
        print('Player 2\'s deck:', p2[::-1])

        if tuple(p1) in seen[1]:
            print("Player 1 cards seen before")
            return 1
        seen[1].add(tuple(p1))
        if tuple(p2) in seen[2]:
            print("Player 1 cards seen before")
            return 1
        seen[2].add(tuple(p2))

        top1 = p1.pop()
        top2 = p2.pop()
        print('Player 1 plays:', top1)
        print('Player 2 plays:', top2)

        if len(p1) >= top1 and len(p2) >= top2:
            print('Playing a sub-game to determine the winner...')
            print()
            winner = game(p1[-top1:], p2[-top2:])
            print('The winner of game is player', winner, '!')
            print()
            print('...anyway, back to game.')
        else:
            if top1 > top2:
                winner = 1
            else:
                winner = 2
        print('Player', winner, 'wins round', round, 'of game!')
        print()

        if winner == 1:
            p1.insert(0, top1)
            p1.insert(0, top2)
        else:
            p2.insert(0, top2)
            p2.insert(0, top1)

    if len(p1) > 0:
        return 1
    else:
        return 2

game(p[1], p[2])

def score(p):
    return sum([p[i] * (i+1) for i in range(len(p))])

print("Player 1", score(p[1]))
print("Player 2", score(p[2]))
