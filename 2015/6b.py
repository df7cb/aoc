#!/usr/bin/python3

import re

lights = {}

with open('6.txt') as f:
    for line in f:
        m = re.match('(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)', line)
        op, x0, y0, x1, y1 = m.groups()

        for x in range(int(x0), int(x1)+1):
            for y in range(int(y0), int(y1)+1):
                if f"{x},{y}" not in lights:
                    lights[f"{x},{y}"] = 0
                if op == 'turn on':
                    lights[f"{x},{y}"] += 1
                elif op == 'turn off' and lights[f"{x},{y}"] > 0:
                    lights[f"{x},{y}"] -= 1
                elif op == 'toggle':
                    lights[f"{x},{y}"] += 2

brightness = 0
for light in lights:
    brightness += lights[light]

print(brightness)
