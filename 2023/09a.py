#!/usr/bin/python3

def is_null(l):
    for x in l:
        if x != 0:
            return False
    return True

def compute(history):
    tails = history[-1]

    while not is_null(history):
        print(history, tails)
        history2 = []
        for i in range(len(history) - 1):
            history2.append(history[i+1] - history[i])
        history = history2
        assert len(history) > 0
        tails += history[-1]

    print(history, tails)
    return tails

report = 0

with open("09.txt") as f:
    for line in f:
        history = [int(x) for x in line.split()]
        report += compute(history)

print(report)
