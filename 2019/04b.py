#!/usr/bin/python3

import re

a, b = 347312, 805915

def good(x):
    for i in range(len(x)-1):
        if x[i] > x[i+1]:
            return False

    x = re.sub(r'(\d)\1\1+', '', x)
    x = re.sub(r'(\d)\1\1+', '', x)
    return re.search(r'(\d)\1', x)

num = 0
for x in range(a, b+1):
    if good(str(x)):
        num += 1

print(num)
