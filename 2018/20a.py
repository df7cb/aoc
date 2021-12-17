#!/usr/bin/python3

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

def walk(graph, id, prefix):
    path = prefix
    node = graph[id]
    if node[0] is not None:
        path += node[0]

    if node[1] == []:
        print("Ended", path)
    else:
        for n in node[1]:
            walk(graph, n, path)

walk(graph, 0, '')

#    for p in range(start, end):
#        if regexp[p] == 'N':
#            y -= 1
#        elif regexp[p] == 'S':
#            y += 1
#        elif regexp[p] == 'W':
#            x -= 1
#        elif regexp[p] == 'E':
#            x += 1
#    print("Walked to", x, y)
