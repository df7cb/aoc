#!/usr/bin/python3

import re
from collections import deque

valve = {}
tunnels = {}

with open("16.txt") as f:
    for line in f:
        print(line)
        m = re.match('Valve (.*) has flow rate=(\d+); tunnels? leads? to valves? (.*)', line)
        valve[m.group(1)] = int(m.group(2))
        tunnels[m.group(1)] = m.group(3).split(', ')

print(valve)
print(tunnels)

# minute, pos, walk, open, flow
status = (0, 'AA', ('AA',), tuple(), 0)

queue = deque([status])

s = 0
max_flow = 0
seen = {}
while queue:
    minute, pos, walk, opens, flow = queue.popleft()
    s += 1
    if s % 10000 == 0:
        print(minute, pos, walk, opens, flow)
    if minute == 30:
        max_flow = max(flow, max_flow)
        continue
    if valve[pos] > 0 and pos not in opens:
        new = (pos, (pos,), tuple(sorted(opens + (pos,))))
        fl = flow + sum({valve[x] for x in opens})
        if new not in seen or seen[new] < fl:
            queue.append((minute+1,) + new + (fl,))
            seen[new] = fl
    for t in tunnels[pos]:
        if t not in walk: # don't go back
            new = (t, tuple(sorted(walk + (t,))), opens)
            fl = flow + sum({valve[x] for x in opens})
            if new not in seen or seen[new] < fl:
                queue.append((minute+1,) + new + (fl,))
                seen[new] = fl

print("max flow is", max_flow)
