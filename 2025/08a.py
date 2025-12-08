#!/usr/bin/python3

from math import sqrt

boxes = []

with open("08.txt") as f:
    for line in f:
        boxes.append([int(x) for x in line.split(',')])

print(boxes)

def dist(a, b):
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)

dists = {}
circuit = {}

for i in range(len(boxes)):
    circuit[i] = set([i])
    for j in range(i+1, len(boxes)):
        d = dist(boxes[i], boxes[j])
        print(i, j, d)
        assert(d not in dists)
        dists[d] = (i, j)

n = 0
for d in sorted(dists.keys()):
    i, j = dists[d]
    a, b = boxes[i], boxes[j]
    u = circuit[i].union(circuit[j])
    for k in u:
        circuit[k] = u
    print(d, i, j, a, b, circuit[i], circuit[j])
    n += 1
    if (n == 1000): break

circuits = set([tuple(x) for x in circuit.values()])

big_circuits = sorted(circuits, key=len)
print(big_circuits)

print(len(big_circuits[-3]) * len(big_circuits[-2]) * len(big_circuits[-1]))
