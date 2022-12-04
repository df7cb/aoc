#!/usr/bin/python3

total = 0

with open("02.txt") as f:
    for line in f:
        op = ord(line[0]) - 65
        res = line[2]

        if res == 'X':
            my = (op-1) % 3
        elif res == 'Y':
            my = op
        elif res == 'Z':
            my = (op+1) % 3

        score = my+1
        if op == my:
            score += 3
        elif my == (op + 1) % 3:
            score += 6
        print(op, my, score)
        total += score

print(total)
