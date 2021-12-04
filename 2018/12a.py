#!/usr/bin/python3

import re

rules = {}
extra_space = 30

with open('12.txt') as f:
    m = re.match('initial state: (.*)', f.readline())
    initial_state = m.group(1)
    f.readline()
    for line in f:
        m = re.match('(.....) => (.)', line)
        rules[m.group(1)] = m.group(2)

print(initial_state)
print(rules)

state = list('.'*extra_space + initial_state + '.'*extra_space)
print(''.join(state))

for round in range(20):
    state2 = ['.', '.']
    for pos in range(2, len(state) - 2):
        sub = ''.join(state[pos-2:pos+3])
        #print("looking at", sub, rules[sub])
        if sub in rules:
            state2.append(rules[sub])
        else:
            state2.append('.')
    state2.extend(['.', '.'])
    state = state2
    print(''.join(state))

val = 0
for pos in range(0, len(state)):
    if state[pos] == '#':
        val += pos - extra_space

print(val)
