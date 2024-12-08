#!/usr/bin/python3

def evals(values):
    if len(values) == 1:
        yield values[0]
    else:
        for v in evals(values[:-1]):
            yield v + values[-1]
            yield v * values[-1]
            yield int(str(v) + str(values[-1]))

def check(res, values):
    for v in evals(values):
        if res == v:
            return True
    return False

calibration = 0

with open("07.txt") as f:
    for line in f:
        res, _, values = line.partition(": ")
        res = int(res)
        values = [int(x) for x in values.split()]
        print(res, values)
        if check(res, values):
            calibration += res

print(calibration)
