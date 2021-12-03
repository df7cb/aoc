#!/usr/bin/python3

# 416 players; last marble is worth 71617 points

#players, last_marble = 9, 25
#players, last_marble = 10, 1618
#players, last_marble = 13, 7999
players, last_marble = 416, 71617

def print_ring(player, ring, current_pos):
    print('['+player+'] ', end='')
    for m in range(len(ring)):
        print("%3s" % (('(' if m == current_pos else ' ') + str(ring[m])), end='')
        if m == current_pos:
            print(')', end='')
        else:
            print('', end='')
    print()

scores = [0 for x in range(players)]
ring = [0]
current_player = 0
current_pos = 0

#print_ring('-', ring, current_pos)

for i in range(1, last_marble+1):
    if i % 23 == 0:
        remove_pos = (current_pos - 7) % len(ring)
        scores[current_player] += i + ring[remove_pos]
        ring = ring[:remove_pos] + ring[remove_pos+1:]
        current_pos = remove_pos % len(ring)
    else:
        insert_pos = (current_pos + 1) % len(ring) + 1
        ring = ring[:insert_pos] + [i] + ring[insert_pos:]
        current_pos = insert_pos

    #print_ring(str(current_player+1), ring, current_pos)

    current_player = (current_player + 1) % players

#print(scores)
print(max(scores))
