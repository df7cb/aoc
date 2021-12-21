#!/usr/bin/python3

from collections import defaultdict
import heapq

# the regexp is long
import sys
sys.setrecursionlimit(10000)

with open('20.txt') as f:
    regexp = f.readline().strip()[1:-1]

print(regexp)

def make_graph(regexp):
    head = 0
    heads = [0]
    branches = [0]
    graph = { 0: (None, []) } # { id: ('NSEW', [id0, ...]), ... }
    id = 1

    #print(' ', head, heads, branches, graph)

    for c in regexp:
        if c in 'NSEW':
            graph[id] = (c, [])
            if head is not None:
                graph[head][1].append(id)
            head = id
            heads[-1] = head
            id += 1
        elif c == '(':
            graph[id] = (None, [])
            branches.append(id)
            graph[head][1].append(id)
            head = id
            heads[-1] = head
            id += 1
        elif c == '|':
            head = branches[-1]
            heads.append(head)
        elif c == ')':
            graph[id] = (None, [])
            for n in heads:
                graph[n][1].append(id)
            head = id
            heads = [head]
            branches.pop()
            id += 1

        #print(c, "head", head, "heads", heads, "branches", branches, graph)

    # closing
    graph[id] = (None, [])
    for n in heads:
        graph[n][1].append(id)
    head = id
    heads = [head]

    #print(c, "head", head, "heads", heads, "branches", branches, graph)

    return graph

graph = make_graph(regexp)

print("Graph nodes:", len(graph))

doors = defaultdict(set)
x, y = 0, 0
visited = set()

def walk(graph, id, x, y):
    if (id, x, y) in visited:
        return
    visited.add((id, x, y))

    node = graph[id]
    if node[0] is not None:
        if node[0] == 'N':
            doors[x,y].add((x,y-1))
            doors[x,y-1].add((x,y))
            y -= 1
        elif node[0] == 'S':
            doors[x,y].add((x,y+1))
            doors[x,y+1].add((x,y))
            y += 1
        elif node[0] == 'W':
            doors[x,y].add((x-1,y))
            doors[x-1,y].add((x,y))
            x -= 1
        elif node[0] == 'E':
            doors[x,y].add((x+1,y))
            doors[x+1,y].add((x,y))
            x += 1

    for n in node[1]:
        walk(graph, n, x, y)

walk(graph, 0, 0, 0)

print("Doors:", doors)

def dijkstra(doors):
    queue = [(0, 0, 0)] # cost here, (x, y)
    heapq.heapify(queue)
    cost = {(0, 0): 0}

    while len(queue) > 0:
        c, x, y = heapq.heappop(queue)
        cost_here = cost[x, y]
        for node in doors[x, y]:
            if node not in cost or cost[node] > cost_here + 1:
                cost[node] = cost_here + 1
                heapq.heappush(queue, (cost_here + 1, node[0], node[1]))

    return cost

cost = dijkstra(doors)

print("Cost:", cost)

print("Furthest node distance:", max(cost.values()))
