#!/usr/bin/python3

import numpy

good = 0

def check(items):
    d = numpy.sign(items[1] - items[0])

    for i in range(1, len(items)):
        if numpy.sign(items[i] - items[i-1]) != d:
            return False
        if abs(items[i-1] - items[i]) > 3:
            return False
    else:
        return True

with open("02.txt") as f:
    for line in f:
        items = [int(x) for x in line.split()]

        if check(items):
            good += 1
            continue

        for i in range(0, len(items)):
            if check(items[0:i] + items[i+1:]):
                good += 1
                break
        else:
            pass

print(good)
