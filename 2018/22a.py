#!/usr/bin/python3

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

#print(region_type(10,10))

s = 0
for x in range(target[0]+1):
    for y in range(target[1]+1):
        s += region_type(x, y)

print(s)
