#!/usr/bin/python3

import copy
import re
import math

with open('20.txt') as f:
    tiles = f.read().strip().split("\n\n")

tile = {}

for t in tiles:
    m = re.match("Tile (\d+):\n(.*)", t, re.S)
    number, tt = m[1], m[2]
    print(number)

    top_border = tt[0:10]

    left_border = right_border = bottom_border = ''
    content = []
    for i in range(10):
        right_border += tt[9 + 11*i]
        left_border += tt[99 - 11*i]
        bottom_border += tt[108 - i]
    for i in range(8):
        content.append(tt[12+11*i : 20+11*i])

    print(tt, top_border, right_border, bottom_border, left_border)
    tile[number] = {
            "tile": tt,
            "top_border": top_border,
            "right_border": right_border,
            "bottom_border": bottom_border,
            "left_border": left_border,
            "content": content,
            }

    for b0 in ["top_border", "right_border", "bottom_border", "left_border"]:
        for b1 in ["top_border", "right_border", "bottom_border", "left_border"]:
            if b0 == b1: continue
            if tile[number][b0] in (tile[number][b1], tile[number][b1][::-1]):
                print('tile', number, 'has duplicated edges')

ntile = len(tile)
border_len = int(math.sqrt(ntile))
print(ntile, border_len)

def joint_border(tile, a, b):
    for ba in ["top_border", "right_border", "bottom_border", "left_border"]:
        for bb in ["top_border", "right_border", "bottom_border", "left_border"]:
            if tile[a][ba] in (tile[b][bb], tile[b][bb][::-1]):
                return True
    return False

results = []
def placement(map, tiles_left, y, x):
    map2 = map.copy()
    for t in sorted(tiles_left):
        if x == y == 0:
            if t not in ('1019', '1801', '1741', '2473'):
                continue # restrict to precomputed corners
            print("checking", t)
        if x > 0:
            if not joint_border(tile, map[y, x-1], t):
                continue
        if y > 0:
            if not joint_border(tile, map[y-1, x], t):
                continue
        map2[y, x] = t
        if x < border_len - 1:
            m = placement(map2, tiles_left - {t}, y, x+1)
            #if m is not None:
            #    return m
        elif y < border_len - 1:
            m = placement(map2, tiles_left - {t}, y+1, 0)
            #if m is not None:
            #    return m
        else:
            global results
            print('found result map', map2)
            results.append(map2.copy())
            #return map2
    #return None

placement({}, set(tile.keys()), 0, 0)

#map = {(0, 0): '1019', (0, 1): '2617', (0, 2): '2729', (0, 3): '1297', (0, 4): '1873', (0, 5): '1571', (0, 6): '1613', (0, 7): '1997', (0, 8): '3739', (0, 9): '2539', (0, 10): '1031', (0, 11): '1801', (1, 0): '2663', (1, 1): '2063', (1, 2): '3911', (1, 3): '3583', (1, 4): '3701', (1, 5): '3847', (1, 6): '3271', (1, 7): '2803', (1, 8): '3079', (1, 9): '3023', (1, 10): '1087', (1, 11): '3803', (2, 0): '1259', (2, 1): '2017', (2, 2): '3121', (2, 3): '2531', (2, 4): '1123', (2, 5): '2683', (2, 6): '2647', (2, 7): '3259', (2, 8): '1049', (2, 9): '1051', (2, 10): '2087', (2, 11): '1429', (3, 0): '2309', (3, 1): '2521', (3, 2): '2969', (3, 3): '3109', (3, 4): '2707', (3, 5): '2657', (3, 6): '2267', (3, 7): '2297', (3, 8): '3793', (3, 9): '3697', (3, 10): '3067', (3, 11): '1621', (4, 0): '3187', (4, 1): '3541', (4, 2): '1747', (4, 3): '3761', (4, 4): '1697', (4, 5): '3463', (4, 6): '3767', (4, 7): '1597', (4, 8): '2633', (4, 9): '2939', (4, 10): '2003', (4, 11): '3331', (5, 0): '3037', (5, 1): '2213', (5, 2): '2089', (5, 3): '2129', (5, 4): '1723', (5, 5): '2347', (5, 6): '2269', (5, 7): '1039', (5, 8): '2687', (5, 9): '3533', (5, 10): '2027', (5, 11): '3797', (6, 0): '3623', (6, 1): '3557', (6, 2): '1583', (6, 3): '3889', (6, 4): '3517', (6, 5): '2917', (6, 6): '2113', (6, 7): '2203', (6, 8): '3499', (6, 9): '3923', (6, 10): '1381', (6, 11): '2711', (7, 0): '1879', (7, 1): '2417', (7, 2): '3457', (7, 3): '3881', (7, 4): '3347', (7, 5): '1871', (7, 6): '2243', (7, 7): '1637', (7, 8): '2621', (7, 9): '1193', (7, 10): '1471', (7, 11): '2111', (8, 0): '1301', (8, 1): '3257', (8, 2): '3191', (8, 3): '1069', (8, 4): '1553', (8, 5): '2239', (8, 6): '1907', (8, 7): '3709', (8, 8): '3041', (8, 9): '3089', (8, 10): '2161', (8, 11): '1847', (9, 0): '3853', (9, 1): '3929', (9, 2): '1693', (9, 3): '3407', (9, 4): '2777', (9, 5): '3581', (9, 6): '2741', (9, 7): '3863', (9, 8): '3919', (9, 9): '3967', (9, 10): '1619', (9, 11): '3137', (10, 0): '2333', (10, 1): '2957', (10, 2): '1229', (10, 3): '1861', (10, 4): '1523', (10, 5): '1367', (10, 6): '3779', (10, 7): '2909', (10, 8): '2659', (10, 9): '1663', (10, 10): '1033', (10, 11): '1361', (11, 0): '1741', (11, 1): '1559', (11, 2): '2887', (11, 3): '2339', (11, 4): '3571', (11, 5): '1423', (11, 6): '1117', (11, 7): '3083', (11, 8): '2579', (11, 9): '2137', (11, 10): '2543', (11, 11): '2473'}

#print(map)
#print(map[0,0], map[0,border_len-1], map[border_len-1,0], map[border_len-1,border_len-1])
#print(int(map[0,0]) * int(map[0,border_len-1]) * int(map[border_len-1,0]) * int(map[border_len-1,border_len-1]))
#print(tile)

def flip_ew(tile, number):
    for y in range(8):
        tile[number]['content'][y] = tile[number]['content'][y][::-1]
    tile[number]['top_border'] = tile[number]['top_border'][::-1]
    tile[number]['bottom_border'] = tile[number]['bottom_border'][::-1]
    tile[number]['left_border'], tile[number]['right_border'] = tile[number]['right_border'], tile[number]['left_border']

def flip_ns(tile, number):
    tile[number]['content'] = tile[number]['content'][::-1]
    tile[number]['left_border'] = tile[number]['left_border'][::-1]
    tile[number]['right_border'] = tile[number]['right_border'][::-1]
    tile[number]['top_border'], tile[number]['bottom_border'] = tile[number]['bottom_border'], tile[number]['top_border']

def flip_diagonally(tile, number):
    new_content = []
    for x in range(8):
        new_content.append("".join(tile[number]['content'][y][x] for y in range(8)))
    tile[number]['content'] = new_content
    tile[number]['top_border'], tile[number]['right_border'], tile[number]['bottom_border'], tile[number]['left_border'] = tile[number]['left_border'][::-1], tile[number]['bottom_border'][::-1], tile[number]['right_border'][::-1], tile[number]['top_border'][::-1]

def rotate_right(tile, number):
    flip_diagonally(tile, number)
    flip_ew(tile, number)

def rotate_left(tile, number):
    flip_diagonally(tile, number)
    flip_ns(tile, number)

def adjust_left_tile(tile, t0, t1):
    assert joint_border(tile, t0, t1)
    for b0 in ["top_border", "right_border", "bottom_border", "left_border"]:
        for b1 in ["top_border", "right_border", "bottom_border", "left_border"]:
            if tile[t0][b0] in (tile[t1][b1], tile[t1][b1][::-1]):
                if b0 == 'top_border':
                    rotate_right(tile, t0)
                    return
                elif b0 == 'right_border':
                    return
                elif b0 == 'bottom_border':
                    rotate_left(tile, t0)
                    return
                elif b0 == 'left_border':
                    flip_ew(tile, t0)
                    return
    raise SyntaxError('No matching orientation for left tile found')

def adjust_right_tile(tile, t0, t1):
    assert joint_border(tile, t0, t1)
    for b0 in ["top_border", "right_border", "bottom_border", "left_border"]:
        for b1 in ["top_border", "right_border", "bottom_border", "left_border"]:
            if tile[t0][b0] in (tile[t1][b1], tile[t1][b1][::-1]):
                if b0 == 'top_border':
                    rotate_left(tile, t0)
                    return
                elif b0 == 'bottom_border':
                    rotate_right(tile, t0)
                    return
                elif b0 == 'right_border':
                    flip_ew(tile, t0)
                    return
                elif b0 == 'left_border':
                    return
    raise SyntaxError('No matching orientation for right tile found')

def adjust_top_tile(tile, t0, t1):
    assert joint_border(tile, t0, t1)
    for b0 in ["top_border", "right_border", "bottom_border", "left_border"]:
        for b1 in ["top_border", "right_border", "bottom_border", "left_border"]:
            if tile[t0][b0] in (tile[t1][b1], tile[t1][b1][::-1]):
                if b0 == 'top_border':
                    flip_ns(tile, t0)
                    return
                elif b0 == 'bottom_border':
                    return
                else:
                    raise SyntaxError('No matching orientation for top tile found ' + b0)
    raise SyntaxError('No matching orientation for top tile found')

def adjust_bottom_tile(tile, t0, t1):
    assert joint_border(tile, t0, t1)
    for b0 in ["top_border", "right_border", "bottom_border", "left_border"]:
        for b1 in ["top_border", "right_border", "bottom_border", "left_border"]:
            if tile[t0][b0] in (tile[t1][b1], tile[t1][b1][::-1]):
                if b0 == 'bottom_border':
                    flip_ns(tile, t0)
                    return
                elif b0 == 'top_border':
                    return
                else:
                    raise SyntaxError('No matching orientation for bottom tile found')
    raise SyntaxError('No matching orientation for bottom tile found')

def rotate_tiles(tile, map):
    # adjust leftmost column
    for y in range(border_len):
        adjust_left_tile(tile, map[y,0], map[y,1])

    # adjust top left tile
    adjust_top_tile(tile, map[0, 0], map[1, 0])

    # adjust leftmost column
    for y in range(1, border_len):
        adjust_bottom_tile(tile, map[y,0], map[y-1,0])

    # adjust rest of top row
    for x in range(1, border_len):
        adjust_right_tile(tile, map[0, x], map[0, x-1])
        adjust_top_tile(tile, map[0, x], map[1, x])

    # adjust inner tiles
    for y in range(1, border_len):
        for x in range(1, border_len):
            adjust_right_tile(tile, map[y,x], map[y,x-1])
            adjust_bottom_tile(tile, map[y,x], map[y-1,x])
            #print( tile[map[y,x-1]]['right_border'], tile[map[y,x]]['left_border'][::-1])
            assert tile[map[y,x-1]]['right_border'] in (tile[map[y,x]]['left_border'], tile[map[y,x]]['left_border'][::-1])
            #print( tile[map[y-1,x]]['bottom_border'], tile[map[y,x]]['top_border'])
            assert tile[map[y-1,x]]['bottom_border'] in (tile[map[y,x]]['top_border'], tile[map[y,x]]['top_border'][::-1])

def render_tiles(tile):
    out = []
    for y in range(border_len):
        for yy in range(8):
            row = ''
            for x in range(border_len):
                t = map[y,x]
                row += tile[t]['content'][yy]
            out.append(row)
    return out

def grep_seamoster(txt):
    seamonster = ['..................#.',
                  '#....##....##....###',
                  '.#..#..#..#..#..#...']
    out = [list(x) for x in txt]

    found = False
    for l in range(len(txt) - 2):
        for c in range(len(txt[l]) - len(seamonster[0])):
            for m in range(len(seamonster)):
                if not re.match(seamonster[m], txt[l+m][c:]):
                    break
            else:
                print("found at", l, c)
                found = True
                for m in range(len(seamonster)):
                    for cm in range(len(seamonster[m])):
                        if seamonster[m][cm] == '#':
                            out[l+m][c+cm] = 'O'
    return found, out

for map in results:
    print('trying to solve', map)
    tile2 = copy.deepcopy(tile)
    #print_tiles(tile2)
    rotate_tiles(tile2, map)
    out = render_tiles(tile2)
    #print("\n".join(out))
    found, out2 = grep_seamoster(out)
    if found:
        out3 = "\n".join(["".join(x) for x in out2])
        print("\n".join(["".join(x) for x in out2]))
        rough = [x for x in out3 if x == '#']
        print('roughness is', len(rough))
