#!/usr/bin/python3

def josephus(n):
    """https://en.wikipedia.org/wiki/Josephus_problem#Bitwise"""
    bits = bin(n)[2:]
    left_shift = bits[1:] + bits[0]
    return int(left_shift, 2)

elves = 5
print(elves, josephus(elves))

elves = 3014387
print(elves, josephus(elves))
