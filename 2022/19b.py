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
    status['minute'] += 1
    status['ore'] += status['ore_robot']
    status['clay'] += status['clay_robot']
    status['obsidian'] += status['obsidian_robot']
    status['geode'] += status['geode_robot']
    return status

def enqueue(seen, queue, status):
    #ser = f"{status['minute']} {status['ore_robot']} {status['ore']} {status['clay_robot']} {status['clay']} {status['obsidian_robot']} {status['obsidian']} {status['geode_robot']} {status['geode']} {status['next']}"
    ser = f"{status['ore_robot']} {status['ore']} {status['clay_robot']} {status['clay']} {status['obsidian_robot']} {status['obsidian']} {status['geode_robot']} {status['geode']} {status['next']}"
    if not ser in seen:
        queue.append(status)
        seen.add(ser)

def run(i, blueprint):
    status = {'minute': 0,
              'ore_robot': 1, 'ore': 0,
              'clay_robot': 0, 'clay': 0,
              'obsidian_robot': 0, 'obsidian': 0,
              'geode_robot': 0, 'geode': 0,
              'next': None}
    seen = set()
    queue = deque([status])
    best_geodes = 0

    j = 0
    while queue:
        status = queue.popleft()
        j += 1
        if j % 1000000 == 0 or status['geode'] > 8:
            print(status)
            print(i, len(seen), len(queue))
        if status['minute'] == 32:
            #print(status)
            best_geodes = max(best_geodes, status['geode'])
            continue

        if status['next'] == None:
            status2 = copy(status)
            status2['next'] = 'ore_robot'
            enqueue(seen, queue, status2)

            status2 = copy(status)
            status2['next'] = 'clay_robot'
            enqueue(seen, queue, status2)

            if status['clay_robot'] > 0:
                status2 = copy(status)
                status2['next'] = 'obsidian_robot'
                enqueue(seen, queue, status2)

            if status['obsidian_robot'] > 0:
                status2 = copy(status)
                status2['next'] = 'geode_robot'
                enqueue(seen, queue, status2)

        elif status['next'] == 'ore_robot' and status['ore'] >= blueprint['ore_ore']:
            status2 = build(copy(status))
            status2['ore'] -= blueprint['ore_ore']
            status2['ore_robot'] += 1
            status2['next'] = None
            enqueue(seen, queue, status2)

        elif status['next'] == 'clay_robot' and status['ore'] >= blueprint['clay_ore']:
            status2 = build(copy(status))
            status2['ore'] -= blueprint['clay_ore']
            status2['clay_robot'] += 1
            status2['next'] = None
            enqueue(seen, queue, status2)

        elif status['next'] == 'obsidian_robot' and status['ore'] >= blueprint['obsidian_ore'] and status['clay'] >= blueprint['obsidian_clay']:
            status2 = build(copy(status))
            status2['ore'] -= blueprint['obsidian_ore']
            status2['clay'] -= blueprint['obsidian_clay']
            status2['obsidian_robot'] += 1
            status2['next'] = None
            enqueue(seen, queue, status2)

        elif status['next'] == 'geode_robot' and status['ore'] >= blueprint['geode_ore'] and status['obsidian'] >= blueprint['geode_obsidian']:
            status2 = build(copy(status))
            status2['ore'] -= blueprint['geode_ore']
            status2['obsidian'] -= blueprint['geode_obsidian']
            status2['geode_robot'] += 1
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
