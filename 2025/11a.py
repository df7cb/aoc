#!/usr/bin/python3

connections = {}

with open("11.txt") as f:
    for line in f:
        l, r = line.split(": ")
        connections[l] = r.split()

print(connections)

num = 0

def walk(node, path):
    global num
    if node == "out":
        print(path)
        num += 1
        return

    for n in connections[node]:
        walk(n, path + [n])

walk("you", ["you"])

print(num)
