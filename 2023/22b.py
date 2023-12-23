#!/usr/bin/python3

from copy import deepcopy

bricks = []
tower = {}

with open("22.txt") as f:
    for line in f:
        l, r = line.strip().split('~')
        l = [int(x) for x in l.split(',')]
        r = [int(x) for x in r.split(',')]
        n = len(bricks)

        brick = []
        if l[0] < r[0]:
            for i in range(l[0], r[0]+1):
                pixel = (i, l[1], l[2])
                brick.append(pixel)
                assert pixel not in tower
                tower[pixel] = n
        elif l[1] < r[1]:
            for i in range(l[1], r[1]+1):
                pixel = (l[0], i, l[2])
                brick.append(pixel)
                assert pixel not in tower
                tower[pixel] = n
        elif l[2] < r[2]:
            for i in range(l[2], r[2]+1):
                pixel = (l[0], l[1], i)
                brick.append(pixel)
                assert pixel not in tower
                tower[pixel] = n
        else:
            assert l == r
            pixel = (l[0], l[1], l[2])
            brick.append(pixel)
            assert pixel not in tower
            tower[pixel] = n

        bricks.append(brick)

def height(tower):
    return max(pixel[2] for pixel in tower)

print(height(tower))

def gravity(tower, bricks):
    falling = True
    falls = set()
    while falling:
        falling = False
        for i in range(len(bricks)):
            if bricks[i] == []: continue
            fall = min(((x, y, z-1) not in tower or tower[(x, y, z-1)]==i) and z > 1 for x, y, z in bricks[i])
            if fall:
                #print(f"Brick {i} {bricks[i]} can fall {fall}")
                falls.add(i)
                for b in range(len(bricks[i])):
                    pixel = bricks[i][b]
                    del tower[pixel]
                    pixel = (pixel[0], pixel[1], pixel[2]-1)
                    bricks[i][b] = pixel
                    tower[pixel] = i
                falling = True
    return len(falls)

gravity(tower, bricks)

print(height(tower))

n = 0
for i in range(len(bricks)):
    t = deepcopy(tower)
    b = deepcopy(bricks)
    for pixel in b[i]:
        del t[pixel]
    b[i] = []
    falls = gravity(t, b)
    n += falls
    print(f"If brick {i} were removed, {falls} bricks would fall")

print(n)
