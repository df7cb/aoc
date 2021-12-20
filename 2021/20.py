#!/usr/bin/python3

with open('20.txt') as f:
    algo = f.readline().strip()
    f.readline()
    image = [line.strip() for line in f]

print(algo)

print("Before")
for line in image:
    print(line)
print()

def value(image, y, x, default):
    if y < 0 or y >= len(image) or x < 0 or x >= len(image[0]):
        return int(default == '#')
    return int(image[y][x] == '#')

def enhance(algo, image, y, x, default):
    bits = 0
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            bits *= 2
            bits += value(image, y+dy, x+dx, default)
    return algo[bits]

def step(algo, image, default):
    image2 = []
    for y in range(-1, len(image)+1):
        line = []
        for x in range(-1, len(image[0])+1):
            line.append(enhance(algo, image, y, x, default))
        image2.append(''.join(line))
    return image2

image = step(algo, image, algo[-1])
image = step(algo, image, algo[0])

print("After 2")
count = 0
for line in image:
    print(line)
    for c in line:
        if c == '#':
            count += 1

print(count)

for i in range(24):
    image = step(algo, image, algo[-1])
    image = step(algo, image, algo[0])

print("After 50")
count = 0
for line in image:
    print(line)
    for c in line:
        if c == '#':
            count += 1

print(count)
