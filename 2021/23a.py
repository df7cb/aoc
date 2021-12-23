#!/usr/bin/python3

###########1#
#01.3.5.7.90#
###D#C#A#B###
  #C#D#A#B#
  #########

chambers = [['C', 'D'], ['D', 'C'], ['A', 'A'], ['B', 'B']]

#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########

chambers = [['A', 'B'], ['D', 'C'], ['C', 'B'], ['A', 'D']]

want_chambers = [['A', 'A'], ['B', 'B'], ['C', 'C'], ['D', 'D']]
hallway = ['.' for x in range(11)]
hallway_places = [0, 1, 3, 5, 7, 9, 10]

print(hallway)
print(chambers)

def is_free(hallway, a, b):
    l, r = min(a,b), max(a,b)
    #print("is_free", hallway, a, b, l, r)
    for x in [x for x in range(l+1, r)] + [b]:
        if hallway[x] != '.':
            return False
    return True

def chamber_exit(ch):
    return 2 * (ch+1)

def reachable_hallway(hallway, ch):
    assert(0 <= ch <= 3)
    ch_exit = chamber_exit(ch)
    ha = []
    for h in hallway_places:
        if is_free(hallway, ch_exit, h):
            ha.append(h)
    return ha

def reachable_chamber(hallway, n, ch):
    ch_exit = chamber_exit(ch)
    return is_free(hallway, n, ch_exit)

def hallway_cost(ha, ch):
    ch_exit = chamber_exit(ch)
    c = abs(ha - ch_exit)
    return c + 1 # one extra for moving to chamber

def amphipod_cost(a):
    if a == 'A':
        return 1
    elif a == 'B':
        return 10
    elif a == 'C':
        return 100
    elif a == 'D':
        return 1000
    else:
        assert(0)

best_cost = 100000
def walk(hallway, chambers, cost, level):
    if chambers == want_chambers:
        global best_cost
        if cost < best_cost:
            best_cost = cost
            print("Found solution with cost", cost, "best so far:", best_cost)
        return

    if level <= 3:
        print("    "*level + "Looking at", hallway, chambers, cost, best_cost)
    # move one amphipod from the chambers to the hallway
    for ch in range(len(chambers)):
        if len(chambers[ch]) > 0:
            #print("    "*level + "for chamber", ch, "reachable hallway is", reachable_hallway(hallway, ch))
            for ha in reachable_hallway(hallway, ch):
                new_hallway = [x for x in hallway]
                new_chambers = [[x for x in ch] for ch in chambers]

                amphipod = new_chambers[ch].pop()
                amphipod_n = ord(amphipod) - 65
                if amphipod_n == ch and not (len(new_chambers[ch]) == 1 and new_chambers[ch][0] != ch):
                    break # don't move out of target chamber unless blocking something
                new_hallway[ha] = amphipod
                new_cost = hallway_cost(ha, ch)
                if len(new_chambers[ch]) == 0:
                    new_cost += 1
                new_cost *= amphipod_cost(amphipod)
                #print("    "*level + "Moving", amphipod, "to", ha, "with cost", new_cost)
                walk(new_hallway, new_chambers, cost + new_cost, level+1)

    # move one amphipod from the hallway to the chambers
    for ha in range(len(hallway)):
        if hallway[ha] == '.':
            continue
        amphipod = hallway[ha]
        amphipod_n = ord(amphipod) - 65
        #print("    "*level + "Considering amphipod", amphipod, "at position", ha)
        if (len(chambers[amphipod_n]) == 0 or \
           len(chambers[amphipod_n]) == 1 and chambers[amphipod_n][0] == amphipod) and \
           reachable_chamber(hallway, ha, amphipod_n):
               new_hallway = [x for x in hallway]
               new_chambers = [[x for x in ch] for ch in chambers]
               new_hallway[ha] = '.'
               new_chambers[amphipod_n].append(amphipod)
               new_cost = hallway_cost(ha, ch)
               if len(new_chambers[ch]) == 1:
                   new_cost += 1
               new_cost *= amphipod_cost(amphipod)
               #print("    "*level + "Amphipod", amphipod, "can move to chamber", amphipod_n, "at cost", new_cost)
               walk(new_hallway, new_chambers, cost + new_cost, level+1)

walk(hallway, chambers, 0, 0)

print("Found best solution with cost", best_cost)
