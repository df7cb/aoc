#!/usr/bin/python3

timestamp = 1003681
busses = '23,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,431,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,19,x,x,x,x,x,x,x,x,x,x,x,409,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29'

schedule = busses.split(',')

print(schedule)

for bus in schedule:
    if bus == 'x':
        continue

    wait = int(bus) - (timestamp % int(bus))
    print(wait, wait * int(bus))
