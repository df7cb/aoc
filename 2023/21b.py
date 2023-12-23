#!/usr/bin/python3

with open("21.txt") as f:
    garden = [line.strip() for line in f]

for y in range(len(garden)):
    if 'S' in garden[y]:
        x = garden[y].index('S')
        break

spots = set([(y, x)])
print(spots)

def print_garden(garden, spots):
    for y in range(len(garden)):
        for x in range(len(garden[0])):
            if (y, x) in spots: print('O', end='')
            else: print(garden[y][x], end='')
        print()

def move(spots):
    spots2 = set()

    for y, x in spots:
        for y2, x2 in ((y, x-1), (y, x+1), (y-1, x), (y+1, x)):
            if x2 >= 0 and x2 < len(garden[0]) and y2 >= 0 and y2 < len(garden):
                if garden[y2][x2] in ('.', 'S'):
                    spots2.add((y2, x2))

    return spots2

print_garden(garden, spots)

extra = 66
extra2 = 131
for i in range(131):
    spots = move(spots)
    #print_garden(garden, spots)
    print(i+1, len(spots))
    if i+1 == 130:
        even = len(spots)
        e1 = sum(1 for y, x in spots if y+x <= extra)
        e2 = sum(1 for y, x in spots if len(garden)-1-y+x <= extra)
        e3 = sum(1 for y, x in spots if y+len(garden[0])-1-x <= extra)
        e4 = sum(1 for y, x in spots if len(garden)-1-y+len(garden[0])-1-x <= extra)
    elif i+1 == 131:
        odd = len(spots)
        o1 = sum(1 for y, x in spots if y+x <= extra2+extra)
        o2 = sum(1 for y, x in spots if len(garden)-1-y+x <= extra2+extra)
        o3 = sum(1 for y, x in spots if y+len(garden[0])-1-x <= extra2+extra)
        o4 = sum(1 for y, x in spots if len(garden)-1-y+len(garden[0])-1-x <= extra2+extra)

        oe1 = sum(1 for y, x in spots if y+x <= extra2+extra or len(garden)-1-y+x <= extra2+extra)
        oe2 = sum(1 for y, x in spots if len(garden)-1-y+x <= extra2+extra or len(garden)-1-y+len(garden[0])-1-x <= extra2+extra)
        oe3 = sum(1 for y, x in spots if len(garden)-1-y+len(garden[0])-1-x <= extra2+extra or y+len(garden[0])-1-x <= extra2+extra)
        oe4 = sum(1 for y, x in spots if y+len(garden[0])-1-x <= extra2+extra or y+x <= extra2+extra)
print(odd, even)
print(e1, e2, e3, e4)
print(o1, o2, o3, o4)
print(oe1, oe2, oe3, oe4)

def center_squares(n):
    o = 1
    e = 0
    i = 0
    while i < n:
        o += 4*i
        i += 1
        if i>=n: break
        e += 4*i
        i += 1
    return o, e

n = 202300
o, e = center_squares(n)
print(o, e)

# answer is between 613391294555255 and 613391400559675
print(o * odd + e * even + (n-1)*(e1+e2+e3+e4) + (n-2)*(o1+o2+o3+o4) + (oe1+oe2+oe3+oe4))

# 65 131 = 65 130 -> 613391294555255 low
# 66 130          -> 613391348771387
# 66 131          -> 613391400559675 high
# n=202301           613397336881656 high
