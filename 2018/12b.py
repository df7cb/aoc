#!/usr/bin/python3

import re
from collections import deque

rules = {}

def value(state, offset):
    val = 0
    for pos in range(0, len(state)):
        if state[pos] == '#':
            val += pos + offset
    return val

with open('12.txt') as f:
    m = re.match('initial state: (.*)', f.readline())
    initial_state = m.group(1)
    f.readline()
    for line in f:
        m = re.match('(.....) => (.)', line)
        rules[m.group(1)] = m.group(2)

print(initial_state)
#print(rules)

offset = -3
state = deque('...' + initial_state + '...')
print(0, offset, ''.join(state))

for round in range(200):
    state2 = deque(['.', '.'])
    for pos in range(2, len(state) - 2):
        sub = state[pos-2] + state[pos-1] + state[pos] + state[pos+1] + state[pos+2]
        #print("looking at", sub, rules[sub])
        if sub in rules:
            state2.append(rules[sub])
        else:
            state2.append('.')

    if state2[2] == '#':
        state2.appendleft('.')
        offset -= 1
    if state2[2] == '.' and state2[3] == '.':
        state2.popleft()
        offset += 1
    if state2[2] == '.' and state2[3] == '.':
        state2.popleft()
        offset += 1

    state2.append('.')
    state2.append('.')
    if state2[-4] == '#' or state2[-3] == '#':
        state2.append('.')
    if state2[-4] == '#' or state2[-3] == '#':
        state2.append('.')

    state = state2
    print(round, offset, ''.join(state))
    if round == 19:
        print(round, offset, value(state, offset))

print(round, offset, value(state, offset))

# steady state reached now

offset += 50000000000 - 200

print(round, offset, value(state, offset))
