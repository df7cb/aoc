#!/usr/bin/python3

with open('13.txt') as f:
    track = f.readlines()

directions = {
        '<': (0, -1),
        '>': (0,  1),
        '^': (-1, 0),
        'v': ( 1, 0),
        }

carts = []
nr = 0

for y in range(len(track)):
    for x in range(len(track[y])):
        if track[y][x] in ('<', '>', '^', 'v'):
            cart = {'nr': nr, 'y': y, 'x': x, 'dir': directions[track[y][x]], 'count': 0}
            carts.append(cart)
            nr += 1

print(carts)

def left(dir):
    return (-dir[1], dir[0])

def right(dir):
    return (dir[1], -dir[0])

tick = 0
while True:
    print("Tick", tick)
    for cart in sorted(carts, key=lambda c: (c['y'], c['x'])):
        print(cart)

        # moving
        cart['y'] += cart['dir'][0]
        cart['x'] += cart['dir'][1]

        # collision detection
        for cart2 in carts:
            if cart2['nr'] == cart['nr']:
                continue
            if cart2['x'] == cart['x'] and cart2['y'] == cart['y']:
                print("Collision!")
                print(cart)
                print(cart2)
                exit(0)

        # turning
        if track[cart['y']][cart['x']] == '/':
            if cart['dir'][0] != 0: # going vertical
                cart['dir'] = right(cart['dir'])
            else:
                cart['dir'] = left(cart['dir'])
        elif track[cart['y']][cart['x']] == '\\':
            if cart['dir'][0] != 0: # going vertical
                cart['dir'] = left(cart['dir'])
            else:
                cart['dir'] = right(cart['dir'])
        elif track[cart['y']][cart['x']] == '+':
            if cart['count'] == 0:
                cart['dir'] = left(cart['dir'])
            elif cart['count'] == 2:
                cart['dir'] = right(cart['dir'])
            cart['count'] = (cart['count'] + 1) % 3;

    tick += 1
