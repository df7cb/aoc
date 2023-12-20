#!/usr/bin/python3

from collections import deque

import re

module = {'output': {'type': '', 'out': [], 'in': {}}}

with open("20.txt") as f:
    for line in f:
        m = re.match('([&%]?)(\w+) -> (.*)', line)
        module[m.group(2)] = {
                'type': m.group(1),
                'out': m.group(3).split(', '),
                'in': {},
                }
        if m.group(1) == '%':
            module[m.group(2)]['state'] = 0

for m in [x for x in module]:
    for out in module[m]['out']:
        if out not in module:
            module[out] = {'type': '', 'out': [], 'in': {}}

        module[out]['in'][m] = 0

print(module)

count = {0: 0, 1: 0}

def push_button():
    signals = deque([('button', 0, 'broadcaster')])

    while signals:
        source, signal, dest = signals.popleft()
        count[signal] += 1
        md = module[dest]
        print(f"{source} -{'high' if signal else 'low'}-> {dest} {md}")
        if md['type'] == '':
            for out in md['out']:
                signals.append((dest, signal, out))
        elif md['type'] == '%':
            if signal == 0:
                md['state'] = 1 - md['state']
                for out in md['out']:
                    signals.append((dest, md['state'], out))
        elif md['type'] == '&':
            md['in'][source] = signal
            memory = min(md['in'].values())
            for out in md['out']:
                signals.append((dest, 1 - memory, out))

    print()

for i in range(1000):
    push_button()

print(count)
print(count[0] * count[1])
