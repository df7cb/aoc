#!/usr/bin/python3

import re

lights = {}

with open('6.txt') as f:
    for line in f:
        m = re.match('(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)', line)
        op, x0, y0, x1, y1 = m.groups()

        for x in range(int(x0), int(x1)+1):
            for y in range(int(y0), int(y1)+1):
                if op == 'turn on':
                    lights[f"{x},{y}"] = True
                elif op == 'turn off' and f"{x},{y}" in lights:
                    del lights[f"{x},{y}"]
                elif op == 'toggle':
                    if f"{x},{y}" in lights:
                        del lights[f"{x},{y}"]
                    else:
                        lights[f"{x},{y}"] = True

print(len(lights))
