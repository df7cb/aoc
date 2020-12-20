#!/usr/bin/python3

import re
import math

with open('20.txt') as f:
    tiles = f.read().strip().split("\n\n")

tile = {}

for t in tiles:
    m = re.match("Tile (\d+):\n(.*)", t, re.S)
    number, tt = m[1], m[2]
    print(number)
    print(tt)

    top_border = tt[0:10]

    left_border = right_border = bottom_border = ''
    for i in range(10):
        right_border += tt[9 + 11*i]
        left_border += tt[99 - 11*i]
        bottom_border += tt[108 - i]

    print(top_border, right_border, bottom_border, left_border)
    tile[number] = {
            "tile": tt,
            "top_border": top_border,
            "right_border": right_border,
            "bottom_border": bottom_border,
            "left_border": left_border,
            }

ntile = len(tile)
border_len = int(math.sqrt(ntile))
print(ntile, border_len)

def joint_border(a, b):
    for ba in ["top_border", "right_border", "bottom_border", "left_border"]:
        for bb in ["top_border", "right_border", "bottom_border", "left_border"]:
            if tile[a][ba] in (tile[b][bb], tile[b][bb][::-1]):
                return True
    return False

def placement(map, tiles_left, y, x):
    map2 = map.copy()
    for t in sorted(tiles_left):
        if x > 0:
            if not joint_border(map[y, x-1], t):
                continue
        if y > 0:
            if not joint_border(map[y-1, x], t):
                continue
        map2[y, x] = t
        if x < border_len - 1:
            m = placement(map2, tiles_left - {t}, y, x+1)
            if m is not None:
                return m
        elif y < border_len - 1:
            m = placement(map2, tiles_left - {t}, y+1, 0)
            if m is not None:
                return m
        else:
            return map2
    return None

map = placement({}, set(tile.keys()), 0, 0)

print(map)
print(map[0,0], map[0,border_len-1], map[border_len-1,0], map[border_len-1,border_len-1])
print(int(map[0,0]) * int(map[0,border_len-1]) * int(map[border_len-1,0]) * int(map[border_len-1,border_len-1]))
