#!/usr/bin/python3

import re

tasks = {} # task -> set(prerequisites)
workers = 5
work_timer = [0 for x in range(workers)]
work_job = ['.' for x in range(workers)]
job_extra_time = 60

with open('07.txt') as f:
    for line in f:
        m = re.match('Step (.) must be finished before step (.) can begin.', line)
        (a, b) = m.groups()
        if a not in tasks:
            tasks[a] = set()
        if b not in tasks:
            tasks[b] = set()
        tasks[b].add(a)

def next_task(tasks):
    for t in sorted(tasks):
        if len(tasks[t]) == 0:
            del tasks[t]
            return t

def finish_task(tasks, t):
    for t2 in tasks:
        tasks[t2].discard(t)

tick = 0
while True:
    for w in range(workers):
        if work_timer[w] > 0:
            work_timer[w] -= 1
            if work_timer[w] == 0:
                finish_task(tasks, work_job[w])
                work_job[w] = '.'
    for w in range(workers):
        if work_timer[w] == 0:
            t = next_task(tasks)
            if t is not None:
                print (f"Worker {w} starting {t} at {tick}")
                work_timer[w] = job_extra_time + ord(t) - 64
                work_job[w] = t
    print(tick, work_job, work_timer)

    if len(tasks) == 0 and work_timer == [0 for x in range(workers)]:
        break

    tick += 1
