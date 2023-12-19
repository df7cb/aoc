#!/usr/bin/python3

from random import random

def check(springs, s, head, counts, seen):
    #print(springs, head, counts)
    if (s, head, len(counts)) in seen:
        return seen[(s, head, len(counts))]

    count = 0
    lc = len(counts)
    ls = len(springs)
    sc = sum(counts)
    if s < ls and sc + lc <= ls:
        if springs[s] in ('.', '?'):
            count += check(springs, s+1, '.', counts, seen)
    if lc > 0 and head == '.' and s + sc + lc - 1 <= ls:
        ok = True
        for i in range(counts[0]):
            if springs[s+i] == '.':
                ok = False
                break
        if ok:
            count += check(springs, s+counts[0], '#', counts[1:], seen)
    if lc == 0 and s == len(springs):
        #print(springs, head, counts, "<----------", count)
        count += 1
    #if random() < 0.00001:
    #    print(springs, head, counts, "<----------", count)
    seen[(s, head, len(counts))] = count
    return count

arrangements = 0

with open("12.txt") as f:
    for line in f:
        springs, counts = line.split()
        counts = [int(x) for x in counts.split(',')]
        springs = (springs + '?') * 4 + springs
        counts = counts * 5
        a = check(springs, 0, '.', counts, {})
        arrangements += a
        print(springs, counts, a, arrangements)

print(arrangements)
