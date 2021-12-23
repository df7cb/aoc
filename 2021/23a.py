#!/usr/bin/python3

#############
#01.2.3.4.56#
###D#C#A#B###
  #C#D#A#B#
  #########

hallway = ['.' for x in range(7)]
chambers = [['C', 'D'], ['D', 'C'], ['A', 'A'], ['B', 'B']]

want_chambers = [['A', 'A'], ['B', 'B'], ['C', 'C'], ['D', 'D']]

print(hallway)
print(chambers)

def reachable_hallway(hallway, ch_exit):
    ha = []
    for h in range(ch_exit): # check way to the left
        if hallway[0:ch_exit] == ['.'] * ch_exit:
            ha.append(h)
    for h in range(ch_exit, 7): # check way to the right
        if hallway[ch_exit:7] == ['.'] * (7-ch_exit):
            ha.append(h)
    return ha

def chamber_exit(ch):
    return ch + 2

def amphipod(a):
    if a == 'A':
        return 1
    elif a = 'B':
        return 10
    elif a = 'C':
        return 100
    else:
        return 1000

def walk(hallway, chambers, cost):
    if chambers == want_chambers:
        print("Found solution with cost", cost)
        return

    for ch in range(len(chambers)):
        if len(chambers[ch]) > 0:
            for ha in reachable_hallway(hallway, chamber_exit(ch)):
                amphipod = chambers[ch][-1]
                print("Moving", chambers[ch][-1], "to", ha)
                walk(hallway[:ha]+[chambers[ch][-1]]+hallway[ha+1:],
                        chambers[:ch] + [chambers[ch][:-1]] + chambers[ch+1:],
                        cost + amphipod_cost(

walk(hallway, chambers, 0)

