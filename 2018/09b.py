#!/usr/bin/python3

from collections import deque

# 416 players; last marble is worth 71617 points

#players, last_marble = 9, 25
#players, last_marble = 10, 1618
#players, last_marble = 13, 7999
#players, last_marble = 416, 71617
players, last_marble = 416, 71617 * 100

def print_ring(i, player, ring, current_pos):
    print('['+player+'] ', end='')
    for m in range(len(ring)):
        print("%3s" % (('(' if m == current_pos else ' ') + str(ring[m])), end='')
        if m == current_pos:
            print(')', end='')
        else:
            print('', end='')
    print()
    print('Round', i)

scores = [0 for x in range(players)]
ring = deque([0])
current_player = 0
current_pos = 0

#print_ring(0, '-', ring, current_pos)

for i in range(1, last_marble+1):
    if i % 23 == 0:
        ring.rotate(7)
        scores[current_player] += i + ring.popleft()
    else:
        ring.rotate(-2)
        ring.appendleft(i)

    #print_ring(i, str(current_player+1), ring, current_pos)

    current_player = (current_player + 1) % players

print(scores)
print(max(scores))
