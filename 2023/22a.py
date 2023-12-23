#!/usr/bin/python3

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

falling = True
while falling:
    falling = False
    for i in range(len(bricks)):
        fall = min(((x, y, z-1) not in tower or tower[(x, y, z-1)]==i) and z > 1 for x, y, z in bricks[i])
        if fall:
            print(f"Brick {i} {bricks[i]} can fall {fall}")
            for b in range(len(bricks[i])):
                pixel = bricks[i][b]
                del tower[pixel]
                pixel = (pixel[0], pixel[1], pixel[2]-1)
                bricks[i][b] = pixel
                tower[pixel] = i
            falling = True

print(height(tower))

needed = set()
for i in range(len(bricks)):
    lower = set()
    for x, y, z in bricks[i]:
        if (x, y, z-1) in tower and tower[(x, y, z-1)] != i:
            lower.add(tower[(x, y, z-1)])
    if len(lower) == 1:
        print(f"Brick {i} {bricks[i]} has only one support")
        needed.add(lower.pop())

print(needed)

n = 0
for i in range(len(bricks)):
    if i not in needed:
        n += 1

print(n)
