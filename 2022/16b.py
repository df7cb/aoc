#!/usr/bin/python3

import re
from collections import deque

valve = {}
tunnels = {}

with open("16.txt") as f:
    for line in f:
        m = re.match('Valve (.*) has flow rate=(\d+); tunnels? leads? to valves? (.*)', line)
        valve[m.group(1)] = int(m.group(2))
        tunnels[m.group(1)] = m.group(3).split(', ')

print(valve)
print(tunnels)

# minute, pos, walk, pos2, walk2, open, flow
status = (0, 'AA', ('AA',), 'AA', ('AA',), tuple(), 0)

queue = deque([status])

s = 0
max_flow = 0
seen = {}
while queue:
    minute, pos, walk, pos2, walk2, opens, flow = queue.popleft()
    s += 1
    if s % 10000 == 0:
        print(minute, pos, walk, pos2, walk2, opens, flow)
    if minute == 26:
        max_flow = max(flow, max_flow)
        continue

    # both open
    if valve[pos] > 0 and pos not in opens and valve[pos2] > 0 and pos2 not in opens:
        new = (pos, (pos,), pos2, (pos2,), tuple(sorted(opens + (pos, pos2))))
        fl = flow + sum({valve[x] for x in opens})
        if new not in seen or seen[new] < fl:
            queue.append((minute+1,) + new + (fl,))
            seen[new] = fl

    # first opens, second walks
    if valve[pos] > 0 and pos not in opens:
        for t2 in tunnels[pos2]:
            if t2 not in walk2: # don't go back
                new = (pos, (pos,), t2, tuple(sorted(walk2 + (t2,))), tuple(sorted(opens + (pos,))))
                fl = flow + sum({valve[x] for x in opens})
                if new not in seen or seen[new] < fl:
                    queue.append((minute+1,) + new + (fl,))
                    seen[new] = fl

    # first walks, second opens
    if valve[pos2] > 0 and pos2 not in opens:
        for t in tunnels[pos]:
            if t not in walk: # don't go back
                new = (t, tuple(sorted(walk + (t,))), pos2, (pos2,), tuple(sorted(opens + (pos2,))))
                fl = flow + sum({valve[x] for x in opens})
                if new not in seen or seen[new] < fl:
                    queue.append((minute+1,) + new + (fl,))
                    seen[new] = fl

    # both walk
    for t in tunnels[pos]:
        if t not in walk: # don't go back
            for t2 in tunnels[pos2]:
                if t not in walk2: # don't go back
                    new = (t, tuple(sorted(walk + (t,))), t2, tuple(sorted(walk2 + (t2,))), opens)
                    fl = flow + sum({valve[x] for x in opens})
                    if new not in seen or seen[new] < fl:
                        queue.append((minute+1,) + new + (fl,))
                        seen[new] = fl

print("max flow is", max_flow)
