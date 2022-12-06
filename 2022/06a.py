#!/usr/bin/python3

with open("06.txt") as f:
    l = f.read()
    print(l)
    for i in range(len(l)):
        if len(set(l[i-4:i])) == 4:
            print(i, l[i-4:i])
            break
