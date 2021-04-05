#!/usr/bin/python3

from collections import deque
import re

with open('08.txt') as f:
    numbers = deque([int(x) for x in f.read().split()])

def process(numbers):
    n_children = numbers.popleft()
    n_metadata = numbers.popleft()
    children = []
    ret = 0
    for i in range(n_children):
        children.append(process(numbers))
        print(children)

    if n_children == 0:
        for i in range(n_metadata):
            ret += numbers.popleft()
        return ret

    for i in range(n_metadata):
        data = numbers.popleft()
        if 1 <= data <= n_children:
            ret += children[data-1]
    return ret

print(process(numbers))
