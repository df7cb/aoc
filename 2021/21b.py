#!/usr/bin/python3

#Player 1 starting position: 6
#Player 2 starting position: 7

#pos = [6, 7]
pos = [4, 8]

configs = {} # turn, pos0, pos1, score0, score1
win = 21

def mod10(x):
    x = x % 10
    return 10 if x == 0 else x

def universes(turn, pos0, pos1, score0, score1):
    #print("Looking at", turn, pos0, pos1, score0, score1)
    if (turn, pos0, pos1, score0, score1) in configs: # known configuration
        return configs[(turn, pos0, pos1, score0, score1)]

    elif score0 >= win:
        return (1, 0)
    elif score1 >= win:
        return (0, 1)

    elif turn == 2:
        s = (0, 0)
        for die in range(1, 4):
            pos0_ = mod10(pos0+die)
            res = universes((turn+1)%6, pos0_, pos1, score0+pos0_, score1)
            s = (s[0]+res[0], s[1]+res[1])
        configs[(turn, pos0, pos1, score0, score1)] = s
        return s
    elif turn == 5:
        s = (0, 0)
        for die in range(1, 4):
            pos1_ = mod10(pos1+die)
            res = universes((turn+1)%6, pos0, pos1_, score0, score1+pos1_)
            s = (s[0]+res[0], s[1]+res[1])
        configs[(turn, pos0, pos1, score0, score1)] = s
        return s
    else:
        s = (0, 0)
        for die in range(1, 4):
            res = universes((turn+1)%6, pos0, pos1, score0, score1)
            s = (s[0]+res[0], s[1]+res[1])
        #configs[(turn, pos0, pos1, score0, score1)] = s
        return s

res = universes(0, pos[0], pos[1], 0, 0)
#for c in configs:
#    print(c, configs[c])
print(len(configs))
print(res)
