#!/usr/bin/python3

import re

finish = 2503

with open('14.txt') as f:
    for line in f:
        m = re.match('(.*) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.', line)
        deer, speed, duration, rest = (m[1], int(m[2]), int(m[3]), int(m[4]))

        cycles = int(finish / (duration+rest))
        last_cycle_time = finish % (duration+rest)

        if last_cycle_time > duration:
            total = (cycles * duration + duration) * speed
        else:
            total = (cycles * duration + last_cycle_time) * speed

        print(deer, speed, duration, rest, cycles, last_cycle_time, total)
