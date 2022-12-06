#!/usr/bin/python3

size = 14

with open("06.txt") as f:
    l = f.read()
    print(l)
    for i in range(len(l)):
        if len(set(l[i-size:i])) == size:
            print(i, l[i-size:i])
            break
