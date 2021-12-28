#!/usr/bin/python3

import heapq

depth = 11820
target = 7,782

#depth = 510
#target = 10,10

geocache = {}
def geologic_index(x,y):
    global geocache
    if (x,y) in geocache:
        return geocache[x,y]
    if (x,y) == (0,0):
        return 0
    elif (x,y) == target:
        return 0
    elif y == 0:
        return x * 16807
    elif x == 0:
        return y * 48271
    else:
        e = erosion_level(x-1,y) * erosion_level(x,y-1)
        geocache[x,y] = e
        return e

def erosion_level(x,y):
    return (geologic_index(x,y) + depth) % 20183

def region_type(x,y):
    reg = erosion_level(x,y) % 3
    return reg
    if reg == 0:
        return "rocky"
    elif reg == 1:
        return "wet"
    elif reg == 2:
        return "narrow"

def compat(reg, tool):
    if reg == 0:
        return tool in (1, 2)
    elif reg == 1:
        return tool in (0, 1)
    elif reg == 2:
        return tool in (0, 2)

#print(region_type(10,10))

#pos = (dist, x, y, tool) # tool: 0-none 1-climb 2-torch

dists = { (0, 0, 2): 0 }
queue = [(0, 0, 0, 2)]
heapq.heapify(queue)

while len(queue) > 0:
    dist, x, y, tool = heapq.heappop(queue)
    print(len(queue), dist, x, y, tool)
    if (x, y) == target and tool == 2:
        print("Found target at distance", dist)
        exit(0)
    this_type = region_type(x, y)
    assert compat(this_type, tool)

    # try to move
    moves = [(x+1,y), (x, y+1), (x-1,y), (x, y-1)]
    for move in moves:
        if move[0] < 0 or move[1] < 0:
            continue
        that_type = region_type(*move)
        if not compat(that_type, tool):
            continue
        if (*move, tool) not in dists or dist+1 < dists[(*move, tool)]:
            heapq.heappush(queue, (dist+1, *move, tool))
            dists[(*move, tool)] = dist+1

    # try to change tool
    new_tool = [x for x in range(3) if x != tool and compat(this_type, x)]
    if (x, y, new_tool[0]) not in dists or dist+7 < dists[(x, y, new_tool[0])]:
        heapq.heappush(queue, (dist+7, x, y, new_tool[0]))
        dists[(x, y, new_tool[0])] = dist+7
