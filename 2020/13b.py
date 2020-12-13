#!/usr/bin/python3

import euclide
import functools

timestamp = 1003681
busses = '23,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,431,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,19,x,x,x,x,x,x,x,x,x,x,x,409,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29'.split(",")

schedule = []
for p in range(len(busses)):
    if busses[p] != 'x':
        schedule.append((int(busses[p]), p+1))

print(schedule)

period, phase = functools.reduce(lambda a, b: euclide.combine_phased_rotations(a[0], a[1], b[0], b[1]), schedule)

print(period, phase, period-phase+1)
