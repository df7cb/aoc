#!/usr/bin/python3

from random import random

def check(springs, s, head, counts, c):
    #print(springs, head, counts)

    count = 0
    lc = len(counts)
    ls = len(springs)
    sc = sum(counts)
    if s < ls and sc + lc <= ls:
        if springs[s] in ('.', '?'):
            count += check(springs, s+1, '.', counts, c)
    if lc > 0 and head == '.' and s + sc + lc - 1 <= ls:
        ok = True
        for i in range(counts[0]):
            if springs[s+i] == '.':
                ok = False
                break
        if ok:
            count += check(springs, s+counts[0], '#', counts[1:], c)
    if lc == 0 and s == len(springs):
        #print(springs, head, counts, "<----------", count)
        return count + 1
    #if random() < 0.00001:
    #    print(springs, head, counts, "<----------", count)
    return count

arrangements = 0

with open("12.txt") as f:
    for line in f:
        springs, counts = line.split()
        springs = (springs + '?') * 4 + springs
        counts = [int(x) for x in counts.split(',')]
        counts = counts * 5
        print(springs, counts)
        a = check(springs, 0, '.', counts, 0)
        arrangements += a
        print(springs, counts, a, arrangements)

print(arrangements)
