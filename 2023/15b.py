#!/usr/bin/python3

def hash(s):
    val = 0
    for c in s:
        val = ((val + ord(c)) * 17) % 256
    return val

boxes = [[] for x in range(256)]

with open("15.txt") as f:
    for s in f.readline().strip().split(','):
        if '-' in s:
            lens = s[:-1]
            box = hash(lens)
            boxes[box] = [x for x in boxes[box] if x[0] != lens]
        else:
            lens, focal = s.split('=')
            box = hash(lens)
            if lens in [x[0] for x in boxes[box]]:
                i = [x[0] for x in boxes[box]].index(lens)
                boxes[box][i] = (lens, int(focal))
            else:
                boxes[box].append((lens, int(focal)))

        print(boxes)

power = 0
for i in range(len(boxes)):
    for j in range(len(boxes[i])):
        power += (1+i) * (1+j) * boxes[i][j][1]

print(power)
