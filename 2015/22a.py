#!/usr/bin/python3

from copy import deepcopy

boss_hit_points = 51
boss_damage = 9
player_hit_points = 50
player_mana = 500

##boss_hit_points = 13
#boss_hit_points = 14
#boss_damage = 8
#player_hit_points = 10
#player_mana = 250

mana_clamp = 1777 # stop search here

spells = {
        "MM": 53, # It instantly does 4 damage.
        "Dr": 73, # It instantly does 2 damage and heals you for 2 hit points.
        "Sh": 113, # It starts an effect that lasts for 6 turns. While it is active, your armor is increased by 7.
        "Po": 173, # It starts an effect that lasts for 6 turns. At the start of each turn while it is active, it deals the boss 3 damage.
        "Re": 229, # It starts an effect that lasts for 5 turns. At the start of each turn while it is active, it gives you 101 new mana.
        }

def play(past_spells, player_mana, mana_spent, player_hit_points, boss_hit_points):
    global mana_clamp
    if mana_spent > mana_clamp:
        return False

    # player's turn
    print(past_spells, player_mana, mana_spent, player_hit_points, boss_hit_points)
    player_mana -= spells[past_spells[-2]] # cost of current spell
    player_damage = 0
    if past_spells[-2] == "MM":
        player_damage += 4
    if past_spells[-2] == "Dr":
        player_damage += 2
        player_hit_points += 2
    if "Po" in past_spells[max(-len(past_spells),-8):-2]:
        player_damage += 3
    if "Re" in past_spells[max(-len(past_spells),-7):-2]:
        player_mana += 101

    #player_damage = max(player_damage, 1)
    boss_hit_points -= player_damage

    if boss_hit_points <= 0:
        print('boss dies', past_spells, player_mana, mana_spent, player_hit_points, boss_hit_points)
        print(mana_spent)
        if mana_spent < mana_clamp:
            mana_clamp = mana_spent
        return True

    # boss' turn
    print(past_spells, player_mana, mana_spent, player_hit_points, boss_hit_points)
    player_armor = 0
    player_damage = 0
    if "Sh" in past_spells[max(-len(past_spells),-7):-1]:
        player_armor += 7

    # poison is active in boss' turn as well
    if "Po" in past_spells[max(-len(past_spells),-7):-1]:
        player_damage += 3
    boss_hit_points -= player_damage
    if boss_hit_points <= 0:
        print('boss dies', past_spells, player_mana, mana_spent, player_hit_points, boss_hit_points)
        print(mana_spent)
        if mana_spent < mana_clamp:
            mana_clamp = mana_spent
        return True

    if "Re" in past_spells[max(-len(past_spells),-6):-1]:
        player_mana += 101

    boss_damage_ = boss_damage - player_armor
    boss_damage_ = max(boss_damage_, 1)
    player_hit_points -= boss_damage_

    if player_hit_points <= 0:
        #print('player dies')
        print(past_spells, player_mana, mana_spent, player_hit_points, boss_hit_points)
        return False

    game(past_spells, player_mana, mana_spent, player_hit_points, boss_hit_points)

def game(past_spells, player_mana, mana_spent, player_hit_points, boss_hit_points):
    found = False
    for spell in spells:
        if player_mana < spells[spell]:
            continue
        play(past_spells+[spell, ''], player_mana, mana_spent + spells[spell], player_hit_points, boss_hit_points)
        found = True
    #if not found:
    #    play(past_spells+['', ''], player_mana, mana_spent, player_hit_points, boss_hit_points)

game([], player_mana, 0, player_hit_points, boss_hit_points)

print(mana_clamp)
