#!/usr/bin/python3

save = 100

from collections import deque

with open("20.txt") as f:
    track = f.readlines()

# find exit

for ey in range(len(track)):
    if 'E' in track[ey]:
        ex = track[ey].index('E')
        break

# compute distances to exit from all reachable cells

dist = {(ey, ex): 0}
queue = deque([(ey, ex, 0)])

while queue:
    y, x, d = queue.popleft()

    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        if (y+dy, x+dx) not in dist and track[y+dy][x+dx] != '#':
            dist[y+dy, x+dx] = d+1
            queue.append((y+dy, x+dx, d+1))

# find start

for sy in range(len(track)):
    if 'S' in track[sy]:
        sx = track[sy].index('S')
        break

print("best distance is", dist[sy, sx])
nocheat = dist[sy, sx]

# run from start

seen = set([(sy, sx)])
queue = deque([(sy, sx, 0)])
cheats = 0
stats = {}

while queue:
    y, x, d = queue.popleft()
    #print(y, x, d)

    if track[y][x] == 'E':
        break

    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        if (y+dy, x+dx) not in seen and track[y+dy][x+dx] != '#':
            seen.add((y+dy, x+dx))
            queue.append((y+dy, x+dx, d+1))

        if 0<=y+2*dy<len(track) and 0<=x+2*dx<len(track[0]) and (y+2*dy, x+2*dx) in dist:
            assert track[y+2*dy][x+2*dx] != '#'
            c = d + 2 + dist[y+2*dy, x+2*dx]
            if c <= nocheat - save:
                print("cheat at", y, x, dy, dx, c, "saves", nocheat - c)
                cheats += 1
                if nocheat - c not in stats:
                    stats[nocheat - c] = 0
                stats[nocheat - c] += 1

print(cheats)
for s in sorted(stats):
    print(f"There are {stats[s]} cheats that save {s} picoseconds.")
