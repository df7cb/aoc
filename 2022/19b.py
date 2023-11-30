#!/usr/bin/python3

import re
from copy import copy
from collections import deque

blueprints = [[]]

with open("19.txt") as f:
    for line in f:
        m = re.match('Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.', line)
        blueprints.append({'ore_ore': int(m.group(2)),
                           'clay_ore': int(m.group(3)),
                           'obsidian_ore': int(m.group(4)),
                           'obsidian_clay': int(m.group(5)),
                           'geode_ore': int(m.group(6)),
                           'geode_obsidian': int(m.group(7))})
        if len(blueprints) > 3:
            break

print(blueprints)

def build(status):
    status['m'] += 1
    status['o'] += status['or']
    status['c'] += status['cr']
    status['O'] += status['Or']
    status['g'] += status['gr']
    return status

def enqueue(seen, queue, status):
    #ser = f"{status['m']} {status['or']} {status['o']} {status['cr']} {status['c']} {status['Or']} {status['O']} {status['gr']} {status['g']} {status['next']}"
    ser = f"{status['or']} {status['o']} {status['cr']} {status['c']} {status['Or']} {status['O']} {status['gr']} {status['g']} {status['next']}"
    if not ser in seen:
        queue.append(status)
        seen.add(ser)

def run(i, blueprint):
    status = {'m': 0,
              'or': 1, 'o': 0,
              'cr': 0, 'c': 0,
              'Or': 0, 'O': 0,
              'gr': 0, 'g': 0,
              'next': None}
    seen = set()
    queue = deque([status])
    best_geodes = 0

    j = 0
    while queue:
        status = queue.popleft()
        j += 1
        if j % 1000000 == 0 or status['g'] > 8:
            print(status)
            print(i, len(seen), len(queue))
        if status['m'] == 32:
            #print(status)
            best_geodes = max(best_geodes, status['g'])
            continue

        if status['next'] == None:
            status2 = copy(status)
            status2['next'] = 'or'
            enqueue(seen, queue, status2)

            status2 = copy(status)
            status2['next'] = 'cr'
            enqueue(seen, queue, status2)

            if status['cr'] > 0:
                status2 = copy(status)
                status2['next'] = 'Or'
                enqueue(seen, queue, status2)

            if status['Or'] > 0:
                status2 = copy(status)
                status2['next'] = 'gr'
                enqueue(seen, queue, status2)

        elif status['next'] == 'or' and status['o'] >= blueprint['ore_ore']:
            status2 = build(copy(status))
            status2['o'] -= blueprint['ore_ore']
            status2['or'] += 1
            status2['next'] = None
            enqueue(seen, queue, status2)

        elif status['next'] == 'cr' and status['o'] >= blueprint['clay_ore']:
            status2 = build(copy(status))
            status2['o'] -= blueprint['clay_ore']
            status2['cr'] += 1
            status2['next'] = None
            enqueue(seen, queue, status2)

        elif status['next'] == 'Or' and status['o'] >= blueprint['obsidian_ore'] and status['c'] >= blueprint['obsidian_clay']:
            status2 = build(copy(status))
            status2['o'] -= blueprint['obsidian_ore']
            status2['c'] -= blueprint['obsidian_clay']
            status2['Or'] += 1
            status2['next'] = None
            enqueue(seen, queue, status2)

        elif status['next'] == 'gr' and status['o'] >= blueprint['geode_ore'] and status['O'] >= blueprint['geode_obsidian']:
            status2 = build(copy(status))
            status2['o'] -= blueprint['geode_ore']
            status2['O'] -= blueprint['geode_obsidian']
            status2['gr'] += 1
            status2['next'] = None
            enqueue(seen, queue, status2)

        else:
            status2 = build(copy(status))
            enqueue(seen, queue, status2)

    print("Best geodes", best_geodes, "blueprint", blueprint)
    return best_geodes

s = 1
for i in range(1, len(blueprints)):
    print(i)
    r = run(i, blueprints[i])
    s *= r
    print("Quality level", r)
print("Product of quality levels", s)
