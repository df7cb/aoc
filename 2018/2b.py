#!/usr/bin/python3

def cmp(l1, l2):
    diff = False
    for c in zip(list(l1), list(l2)):
        if c[0] != c[1]:
            if diff:
                return
            diff = True
    print(l1, l2)
    for c in zip(list(l1), list(l2)):
        if c[0] == c[1]:
            print(c[0], end='')
    print()

with open("2.txt") as f:
    for l in f:
        with open("2.txt") as f2:
            for l2 in f2:
                if l == l2: continue
                cmp(l, l2)

