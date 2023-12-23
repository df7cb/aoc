#!/usr/bin/python3

rounds = 2

with open("21.txt") as f:
    garden = [line.strip() for line in f]

for Y in range(len(garden)):
    if 'S' in garden[Y]:
        X = garden[Y].index('S')
        break

assert garden[Y][X] == 'S'
spots = set([(Y, X)])
#print(spots)

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

steps = 131
print(steps, "steps")
extra = 64
extra2 = 131
for i in range(steps):
    spots = move(spots)
    #print_garden(garden, spots)
    print(i+1, len(spots))
    if i+1 == 65:
        even = len(spots)
        e1 = sum(1 for y, x in spots if y+x <= extra)
        e2 = sum(1 for y, x in spots if len(garden)-1-y+x <= extra)
        e3 = sum(1 for y, x in spots if y+len(garden[0])-1-x <= extra)
        e4 = sum(1 for y, x in spots if len(garden)-1-y+len(garden[0])-1-x <= extra)

        print("odd rhombus")
        print_garden(garden, spots)
        print()

    elif i+1 == 130:
        even = len(spots)
        print("even square")
        print_garden(garden, spots)
        print()
        e1 = set((y, x) for y, x in spots if y+x <= extra)
        print("triangle 1")
        print_garden(garden, e1)
        e1 = len(e1)
        print()
        e2 = set((y, x) for y, x in spots if len(garden)-1-y+x <= extra)
        print("triangle 2")
        print_garden(garden, e2)
        e2 = len(e2)
        print()
        e3 = set((y, x) for y, x in spots if y+len(garden[0])-1-x <= extra)
        print("triangle 3")
        print_garden(garden, e3)
        e3 = len(e3)
        print()
        e4 = set((y, x) for y, x in spots if len(garden)-1-y+len(garden[0])-1-x <= extra)
        print("triangle 3")
        print_garden(garden, e4)
        e4 = len(e4)
        print()


    elif i+1 == 131:
        odd = len(spots)
        print("odd square")
        print_garden(garden, spots)
        print()
        o1 = set((y, x) for y, x in spots if y+x <= extra2+extra)
        print("square without corner 1")
        print_garden(garden, o1)
        o1 = len(o1)
        print()
        o2 = set((y, x) for y, x in spots if len(garden)-1-y+x <= extra2+extra)
        print("square without corner 2")
        print_garden(garden, o2)
        o2 = len(o2)
        print()
        o3 = set((y, x) for y, x in spots if y+len(garden[0])-1-x <= extra2+extra)
        print("square without corner 3")
        print_garden(garden, o3)
        o3 = len(o3)
        print()
        o4 = set((y, x) for y, x in spots if len(garden)-1-y+len(garden[0])-1-x <= extra2+extra)
        print("square without corner 4")
        print_garden(garden, o4)
        o4 = len(o4)
        print()

        oe1 = set((y, x) for y, x in spots if y+x <= extra2+extra and len(garden)-1-y+x <= extra2+extra)
        print("pointy bit 1")
        print_garden(garden, oe1)
        oe1 = len(oe1)
        print()
        oe2 = set((y, x) for y, x in spots if len(garden)-1-y+x <= extra2+extra and len(garden)-1-y+len(garden[0])-1-x <= extra2+extra)
        print("pointy bit 2")
        print_garden(garden, oe2)
        oe2 = len(oe2)
        print()
        oe3 = set((y, x) for y, x in spots if len(garden)-1-y+len(garden[0])-1-x <= extra2+extra and y+len(garden[0])-1-x <= extra2+extra)
        print("pointy bit 3")
        print_garden(garden, oe3)
        oe3 = len(oe3)
        print()
        oe4 = set((y, x) for y, x in spots if y+len(garden[0])-1-x <= extra2+extra and y+x <= extra2+extra)
        print("pointy bit 4")
        print_garden(garden, oe4)
        oe4 = len(oe4)
        print()


# cosmic inflation
Y += rounds * len(garden)
X += rounds * len(garden[0])
for i in range(len(garden)):
    garden[i] = (2*rounds+1) * garden[i]
garden *= (2*rounds+1)
assert garden[Y][X] == 'S'

#print_garden(garden, spots)

steps = rounds * 131 + 65
spots = set([(Y, X)])
print(steps, "steps")
extra = 66
extra2 = 131
for i in range(steps):
    spots = move(spots)
    #print_garden(garden, spots)
    print(i+1, len(spots))
    #if i+1 == 130:
    #    even = len(spots)
    #    e1 = sum(1 for y, x in spots if y+x <= extra)
    #    e2 = sum(1 for y, x in spots if len(garden)-1-y+x <= extra)
    #    e3 = sum(1 for y, x in spots if y+len(garden[0])-1-x <= extra)
    #    e4 = sum(1 for y, x in spots if len(garden)-1-y+len(garden[0])-1-x <= extra)
    #elif i+1 == 131:
    #    odd = len(spots)
    #    o1 = sum(1 for y, x in spots if y+x <= extra2+extra)
    #    o2 = sum(1 for y, x in spots if len(garden)-1-y+x <= extra2+extra)
    #    o3 = sum(1 for y, x in spots if y+len(garden[0])-1-x <= extra2+extra)
    #    o4 = sum(1 for y, x in spots if len(garden)-1-y+len(garden[0])-1-x <= extra2+extra)

    #    oe1 = sum(1 for y, x in spots if y+x <= extra2+extra or len(garden)-1-y+x <= extra2+extra)
    #    oe2 = sum(1 for y, x in spots if len(garden)-1-y+x <= extra2+extra or len(garden)-1-y+len(garden[0])-1-x <= extra2+extra)
    #    oe3 = sum(1 for y, x in spots if len(garden)-1-y+len(garden[0])-1-x <= extra2+extra or y+len(garden[0])-1-x <= extra2+extra)
    #    oe4 = sum(1 for y, x in spots if y+len(garden[0])-1-x <= extra2+extra or y+x <= extra2+extra)

print_garden(garden, spots)
print(i+1, len(spots))

print()
print("odd and even squares:", odd, even)
print("triangles e", e1, e2, e3, e4)
print("squares without corner", o1, o2, o3, o4)
print("pointy ends", oe1, oe2, oe3, oe4)

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

#debug: n = rounds
n = 202300
o, e = center_squares(n)
print("o, e", o, e)

# answer is between 613391294555255 and 613391400559675
print(o * odd + e * even + (n)*(e1+e2+e3+e4) + (n-1)*(o1+o2+o3+o4) + (oe1+oe2+oe3+oe4))

# 65 131 = 65 130 -> 613391294555255 low
# after fixing bugs: 613391294577878
# 66 130          -> 613391348771387
# 66 131          -> 613391400559675 high
# n=202301           613397336881656 high
