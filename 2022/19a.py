#!/usr/bin/python3

import re
from copy import copy as deepcopy
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

print(blueprints)

status = {'minute': 0,
          'ore_robot': 1, 'ore': 0,
          'clay_robot': 0, 'clay': 0,
          'obsidian_robot': 0, 'obsidian': 0,
          'geode_robot': 0, 'geode': 0,
          'next': None}

print(status)

def build(status):
    status['minute'] += 1
    status['ore'] += status['ore_robot']
    status['clay'] += status['clay_robot']
    status['obsidian'] += status['obsidian_robot']
    status['geode'] += status['geode_robot']
    return status

blueprint = blueprints[1]

queue = deque([status])
p = 0
while queue:
    status = queue.popleft()
    #print(status)
    if status['minute'] != p:
        print(status)
        p = status['minute']
    if status['minute'] == 25:
        print(status)
        continue

    if status['next'] == None:
        status2 = build(deepcopy(status))
        status2['next'] = 'ore_robot'
        if status2 not in queue: queue.append(status2)

        status2 = build(deepcopy(status))
        status2['next'] = 'clay_robot'
        if status2 not in queue: queue.append(status2)

        if status['clay_robot'] > 0:
            status2 = build(deepcopy(status))
            status2['next'] = 'obsidian_robot'
            if status2 not in queue: queue.append(status2)

        if status['obsidian_robot'] > 0:
            status2 = build(deepcopy(status))
            status2['next'] = 'geode_robot'
            if status2 not in queue: queue.append(status2)

    if status['next'] == 'ore_robot' and status['ore'] >= blueprint['ore_ore']:
        status2 = build(deepcopy(status))
        status2['ore'] -= blueprint['ore_ore']
        status2['ore_robot'] += 1
        if status2 not in queue: queue.append(status2)

    if status['next'] == 'clay_robot' and status['ore'] >= blueprint['clay_ore']:
        status2 = build(deepcopy(status))
        status2['ore'] -= blueprint['clay_ore']
        status2['clay_robot'] += 1
        if status2 not in queue: queue.append(status2)

    if status['next'] == 'obsidian_robot' and status['ore'] >= blueprint['obsidian_ore'] and status['clay'] >= blueprint['obsidian_clay']:
        status2 = build(deepcopy(status))
        status2['ore'] -= blueprint['obsidian_ore']
        status2['clay'] -= blueprint['obsidian_clay']
        status2['obsidian_robot'] += 1
        if status2 not in queue: queue.append(status2)
        print(status2)

    if status['next'] == 'geode_robot' and status['ore'] >= blueprint['geode_ore'] and status['obsidian'] >= blueprint['geode_obsidian']:
        status2 = build(deepcopy(status))
        status2['ore'] -= blueprint['geode_ore']
        status2['obsidian'] -= blueprint['geode_obsidian']
        status2['geode_robot'] += 1
        if status2 not in queue: queue.append(status2)
        print(status2)

    status2 = build(deepcopy(status))
    if status2 not in queue:
        queue.append(status2)

