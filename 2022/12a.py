#!/usr/bin/python3

from collections import deque

with open("12.txt") as f:
    grid = [line.strip() for line in f]

start = [x for x in range(len(grid)) if grid[x][0] == 'S'][0]
assert start >= 0

#print(grid)

pos = (start, 0)
queue = deque([pos])
visited = {pos: 0}

def height(c):
    if c == 'S':
        return 0
    if c == 'E':
        return 26
    return ord(c) - 97

while len(queue) > 0:
    y, x = queue.popleft()
    #print(y, x)
    curdist = visited[(y, x)]
    if grid[y][x] == 'E':
        print("Found E at distance", curdist)
        exit()

    n = (y, x-1)
    if x > 0 and height(grid[y][x-1]) <= height(grid[y][x]) + 1 and (n not in visited or visited[n] > curdist + 1):
        visited[n] = curdist + 1
        queue.append(n)
    n = (y, x+1)
    if x < len(grid[0])-1 and height(grid[y][x+1]) <= height(grid[y][x]) + 1 and (n not in visited or visited[n] > curdist + 1):
        visited[n] = curdist + 1
        queue.append(n)
    n = (y-1, x)
    if y > 0 and height(grid[y-1][x]) <= height(grid[y][x]) + 1 and (n not in visited or visited[n] > curdist + 1):
        visited[n] = curdist + 1
        queue.append(n)
    n = (y+1, x)
    if y < len(grid)-1 and height(grid[y+1][x]) <= height(grid[y][x]) + 1 and (n not in visited or visited[n] > curdist + 1):
        visited[n] = curdist + 1
        queue.append(n)
