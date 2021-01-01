#!/usr/bin/python3

import re

with open('04.txt') as f:
    lines = f.readlines()

lines.sort()

guard = None
guards = {}
guard_minutes = {}
sleep = None

for line in lines:
    print(line.strip())
    if m := re.match('.....-..-.. (..):(..). Guard #(\d+) begins shift', line):
        hh, mm = int(m[1]), int(m[2])
        guard = int(m[3])
        if hh == 23:
            mm = 0
        if sleep is not None:
            raise Exception('last guard did not wake up')
        if guard not in guards:
            guards[guard] = 0
            guard_minutes[guard] = [0 for x in range(60)]
    elif m := re.match('.....-..-.. (..):(..). falls asleep', line):
        hh, mm = int(m[1]), int(m[2])
        sleep = mm
    elif m := re.match('.....-..-.. (..):(..). wakes up', line):
        hh, mm = int(m[1]), int(m[2])
        print('Guard', guard, 'sleeping from', sleep, 'to', mm)
        guards[guard] += mm - sleep
        for x in range(sleep, mm):
            guard_minutes[guard][x] += 1
        sleep = None

mx = 0
for guard in guards:
    if guards[guard] > mx:
        mx = guards[guard]
        mxguard = guard

print('Guard', mxguard, 'was sleeping', mx)
print(guard_minutes[mxguard])
mxsleep = 0
for mm in range(60):
    if guard_minutes[mxguard][mm] > mxsleep:
        mxsleep = guard_minutes[mxguard][mm]
        mxminute = mm
print('minute most asleep:', mxminute, mxsleep)

print('04a:', mxguard, mxminute, mxguard * mxminute)
