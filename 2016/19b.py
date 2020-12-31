#!/usr/bin/python3

from collections import deque

def white_elephant(n):
    half = int(n/2+1)
    circle1 = deque(range(1, half+1)) # current turn: circle1[0]
    circle2 = deque(range(half+1, n+1)) # 2nd half of circle

    while True:
        if len(circle1) % 10000 == 0:
            print(len(circle1))
        #print(circle1, circle2)
        assert len(circle2) <= len(circle1) <= len(circle2)+1
        if len(circle1) > len(circle2):
            removed = circle1.pop()
        else:
            removed = circle2.popleft()

        if len(circle2) == 0:
            return circle1[0]

        # move to next
        circle1.append(circle2.popleft())
        circle2.append(circle1.popleft())

elves = 5
print(elves, white_elephant(elves))

elves = 3014387
print(elves, white_elephant(elves))
