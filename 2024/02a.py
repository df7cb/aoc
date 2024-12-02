#!/usr/bin/python3

import numpy

good = 0

with open("02.txt") as f:
    for line in f:
        items = [int(x) for x in line.split()]
        d = numpy.sign(items[1] - items[0])

        for i in range(1, len(items)):
            if numpy.sign(items[i] - items[i-1]) != d:
                print("bad dir", items, d)
                break
            if abs(items[i-1] - items[i]) > 3:
                print("bad jump", items)
                break
        else:
            print("good", items)
            good += 1

print(good)
