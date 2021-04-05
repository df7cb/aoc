#!/usr/bin/python3

from collections import deque
import re

with open('08.txt') as f:
    numbers = deque([int(x) for x in f.read().split()])

def process(numbers):
    n_children = numbers.popleft()
    n_metadata = numbers.popleft()
    ret = 0
    for i in range(n_children):
        ret += process(numbers)
    for i in range(n_metadata):
        ret += numbers.popleft()
    return ret

print(process(numbers))
