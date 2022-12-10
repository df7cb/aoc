#!/usr/bin/python3

with open("01.txt") as f:
    print(sum([int(x)//3 - 2 for x in f]))
