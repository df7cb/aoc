#!/usr/bin/python3

with open("11.txt") as f:
    stones = [int(x) for x in f.read().split()]

print(stones)

cache = {}

def step(stone, steps):
    if steps == 0:
        return 1

    if (stone, steps) in cache:
        return cache[(stone, steps)]

    if stone == 0:
        x = step(1, steps - 1)
    elif len(str(stone)) % 2 == 0:
        s = str(stone)
        l = len(s)
        x = step(int(s[:int(l/2)]), steps-1) + step(int(s[int(l/2):]), steps-1)
    else:
        x = step(stone * 2024, steps-1)

    cache[(stone, steps)] = x
    return x

print(sum([step(stone, 75) for stone in stones]))
