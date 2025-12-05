#!/usr/bin/python3

import re

fresh = []

with open("05.txt") as f:
    for line in f:
        if line == "\n": break

        m = re.match(r"(\d+)-(\d+)", line)
        fresh.append((int(m.group(1)), int(m.group(2))))

    count = 0
    for line in f:
        i = int(line)
        for fr in fresh:
            if fr[0] <= i <= fr[1]:
                print(i)
                count += 1
                break

print(count)
