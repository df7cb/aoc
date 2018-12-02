#!/usr/bin/python3

two = 0
three = 0

with open("2.txt") as f:
    for l in f:
        count = {}
        for c in list(l):
            if not c in count:
                count[c] = 0
            count[c] += 1
        for key in count.keys():
            if count[key] == 2:
                two += 1
                break
        for key in count.keys():
            if count[key] == 3:
                three += 1
                break

print(two * three)
