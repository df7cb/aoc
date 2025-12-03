#!/usr/bin/python3

import re

jolts = 0

with open("03.txt") as f:
    for bank in f:
        for j in range(99, 0, -1):
            jj = f"{j:02}"
            l, r = jj[0], jj[1]
            if re.search(f"{l}.*{r}", bank):
                print(bank, l, r)
                jolts += j
                break

print(jolts)
