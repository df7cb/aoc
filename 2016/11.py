#!/usr/bin/python3

"""The first floor contains a promethium generator and a promethium-compatible microchip.
The second floor contains a cobalt generator, a curium generator, a ruthenium generator, and a plutonium generator.
The third floor contains a cobalt-compatible microchip, a curium-compatible microchip, a ruthenium-compatible microchip, and a plutonium-compatible microchip.
The fourth floor contains nothing relevant."""

from collections import deque

# example
#start_building = ( 1, # elevator is on this floor
#        ( ('H', 'M'), ('Li', 'M') ),
#        ( ('H', 'G'), ),
#        ( ('Li', 'G'), ),
#        ( ),
#        )

# 11a:
#start_building = ( 1, # elevator is on this floor
#        ( ('Pm', 'G'), ('Pm', 'M') ),
#        ( ('Cm', 'G'), ('Co', 'G'), ('Pu', 'G'), ('Ru', 'G') ),
#        ( ('Cm', 'M'), ('Co', 'M'), ('Pu', 'M'), ('Ru', 'M') ),
#        ( ),
#        )

# 11b:
start_building = ( 1, # elevator is on this floor
        ( ('D', 'G'), ('D', 'M'), ('E', 'G'), ('E', 'M'), ('Pm', 'G'), ('Pm', 'M') ),
        ( ('Cm', 'G'), ('Co', 'G'), ('Pu', 'G'), ('Ru', 'G') ),
        ( ('Cm', 'M'), ('Co', 'M'), ('Pu', 'M'), ('Ru', 'M') ),
        ( ),
        )

def check(items):
    generators = [x for x in items if x[1]=='G']
    if len(generators) == 0:
        return True
    chips = [x for x in items if x[1]=='M']
    for chip in chips:
        if (chip[0], 'G') not in items:
            return False
    return True

seen = set()
queue = deque([ (0, start_building) ])

old_round_number = None
while len(queue) > 0:
    round_number, building = queue.popleft()
    if old_round_number != round_number:
        print(len(queue), round_number, building)
        old_round_number = round_number
    floor = building[0]

    if floor == 1:
        next_floors = [floor+1]
    elif 2 <= floor <= 3:
        next_floors = [floor-1, floor+1]
    else:
        next_floors = [floor-1]

    for next_floor in next_floors:
        # move one item in elevator
        for item1 in building[floor]:
                floors2 = [0] + list(building[1:])
                floors2[floor] = tuple(x for x in building[floor] if x != item1)
                if not check(floors2[floor]): continue
                floors2[next_floor] = tuple(sorted(building[next_floor] + (item1,)))
                if not check(floors2[next_floor]): continue
                building2 = (next_floor,
                        floors2[1],
                        floors2[2],
                        floors2[3],
                        floors2[4])
                if building2 not in seen:
                    #print("Moving", item1, "from floor", floor, "to floor", next_floor)
                    seen.add(building2)
                    queue.append((round_number + 1, building2))

        # move two items in elevator
        for item1 in building[floor]:
            for item2 in [x for x in building[floor] if x > item1]:
                floors2 = [0] + list(building[1:])
                floors2[floor] = tuple(x for x in building[floor] if x not in (item1, item2))
                if not check(floors2[floor]): continue
                floors2[next_floor] = tuple(sorted(building[next_floor] + (item1, item2)))
                if not check(floors2[next_floor]): continue
                building2 = (next_floor,
                        floors2[1],
                        floors2[2],
                        floors2[3],
                        floors2[4])
                if building2[1:4] == ((),(),()):
                    print("Found solution in round", round_number + 1, building2)
                    exit(0)
                if building2 not in seen:
                    #print("Moving", item1, item2, "from floor", floor, "to floor", next_floor)
                    seen.add(building2)
                    queue.append((round_number + 1, building2))
