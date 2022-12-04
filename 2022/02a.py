#!/usr/bin/python3

total = 0

with open("02.txt") as f:
    for line in f:
        op = ord(line[0]) - 65
        my = ord(line[2]) - 88

        score = my+1
        if op == my:
            score += 3
        elif my == (op + 1) % 3:
            score += 6
        print(op, my, score)
        total += score

print(total)
