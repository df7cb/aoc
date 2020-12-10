#!/usr/bin/python3

import json

with open('12.txt') as f:
    js = json.loads(f.read())

def parse(j):
    sum = 0
    if isinstance(j, dict):
        for key in j:
            sum += parse(j[key])
    elif isinstance(j, list):
        for element in j:
            sum += parse(element)
    elif isinstance(j, str):
        pass
    else:
        sum += j
    return sum

print(parse(js))
