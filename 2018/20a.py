#!/usr/bin/python3

from collections import defaultdict
import heapq

# the regexp is long
import sys
sys.setrecursionlimit(10000)

with open('20.txt') as f:
    regexp = f.readline().strip()[1:-1]

print(regexp)

# xx ( yy | yy ) zz
#         ^ new branch = new head at last branch level
#    ^ new branch level = remember heads for next branch

doors = defaultdict(set)

def parse(regexp, pos, heads, level):
    print("   "*level, "parse", pos, len(heads))
    my_heads = [[[h for h in x] for x in heads]]
    while pos < len(regexp):
        c = regexp[pos]
        pos += 1

        if c in 'NSEW':
            if c == 'N':
                for h in my_heads[-1]:
                    doors[h[0],h[1]].add((h[0],h[1]+1))
                    doors[h[0],h[1]+1].add((h[0],h[1]))
                    h[1] += 1
            elif c == 'S':
                for h in my_heads[-1]:
                    doors[h[0],h[1]].add((h[0],h[1]-1))
                    doors[h[0],h[1]-1].add((h[0],h[1]))
                    h[1] -= 1
            elif c == 'E':
                for h in my_heads[-1]:
                    doors[h[0],h[1]].add((h[0]+1,h[1]))
                    doors[h[0]+1,h[1]].add((h[0],h[1]))
                    h[0] += 1
            elif c == 'W':
                for h in my_heads[-1]:
                    doors[h[0],h[1]].add((h[0]-1,h[1]))
                    doors[h[0]-1,h[1]].add((h[0],h[1]))
                    h[0] -= 1
            print("   "*level, "moved", regexp[pos-1], pos, len(my_heads))

        elif c == '(':
            print("   "*level, "entering", pos, len(my_heads))
            pos, ret = parse(regexp, pos, my_heads[-1], level+1)
            my_heads[-1] = ret
            print("   "*level, "returned", pos, len(my_heads))

        elif c == '|':
            my_heads.append([x for x in heads])
            print("   "*level, "split", pos, len(my_heads))

        elif c == ')':
            break

    ret = set()
    for hs in my_heads:
        for h in hs:
            ret.add((h[0], h[1]))

    print("   "*level, "returning", pos, len(ret))
    return pos, [ [h[0], h[1]] for h in ret ]

print(parse(regexp, 0, [[0,0]], 0))

print("Doors:", doors)

def dijkstra(doors):
    queue = [(0, 0, 0)] # cost here, (x, y)
    heapq.heapify(queue)
    cost = {(0, 0): 0}

    while len(queue) > 0:
        c, x, y = heapq.heappop(queue)
        cost_here = cost[x, y]
        for node in doors[x, y]:
            if node not in cost or cost_here + 1 < cost[node]:
                cost[node] = cost_here + 1
                heapq.heappush(queue, (cost_here + 1, node[0], node[1]))

    return cost

cost = dijkstra(doors)

print("Cost:", cost)

print("Furthest node distance:", max(cost.values()))
