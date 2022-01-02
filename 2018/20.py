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
#    ^ new branch level = remember positions for next branch

doors = defaultdict(set)

def parse(regexp, pos, positions, level):
    print("   "*level, "parse", pos, len(positions))
    my_positions = [positions]
    while pos < len(regexp):
        c = regexp[pos]
        pos += 1

        if c in 'NSEW':
            if c == 'N':
                for p in my_positions[-1]:
                    n = (p[0],p[1]+1)
                    doors[p].add(n)
                    doors[n].add(p)
                my_positions[-1] = { (p[0],p[1]+1) for p in my_positions[-1] }
            elif c == 'S':
                for p in my_positions[-1]:
                    n = (p[0],p[1]-1)
                    doors[p].add(n)
                    doors[n].add(p)
                my_positions[-1] = { (p[0],p[1]-1) for p in my_positions[-1] }
            elif c == 'E':
                for p in my_positions[-1]:
                    n = (p[0]+1,p[1])
                    doors[p].add(n)
                    doors[n].add(p)
                my_positions[-1] = { (p[0]+1,p[1]) for p in my_positions[-1] }
            elif c == 'W':
                for p in my_positions[-1]:
                    n = (p[0]-1,p[1])
                    doors[p].add(n)
                    doors[n].add(p)
                my_positions[-1] = { (p[0]-1,p[1]) for p in my_positions[-1] }
            print("   "*level, "moved", regexp[pos-1], pos, len(my_positions))

        elif c == '(':
            print("   "*level, "entering", pos, len(my_positions))
            pos, ret = parse(regexp, pos, my_positions[-1], level+1)
            my_positions[-1] = ret
            print("   "*level, "returned", pos, len(my_positions))

        elif c == '|':
            my_positions.append([x for x in positions])
            print("   "*level, "split", pos, len(my_positions))

        elif c == ')':
            break

    ret = set()
    for pp in my_positions:
        ret = ret.union(pp)

    print("   "*level, "returning", pos, len(ret))
    return pos, ret

print(parse(regexp, 0, {(0,0)}, 0))

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

far_nodes = 0
for node in cost:
    if cost[node] >= 1000:
        far_nodes += 1
print("Nodes at least 1000 away:", far_nodes)
