#!/usr/bin/python3

from copy import deepcopy

boss = {
        "Name": "Boss",
        "Hit Points": 109,
        "Damage": 8,
        "Armor": 2,
}

player = {
        "Name": "Player",
        "Hit Points": 100,
        "Damage": 0,
        "Armor": 0,
}

weapons = [
        #{ "Name": "None", "Cost": 0, "Damage": 0 },
        { "Name": "Dagger", "Cost": 8, "Damage": 4 },
        { "Name": "Shortsword", "Cost": 10, "Damage": 5 },
        { "Name": "Warhammer", "Cost": 25, "Damage": 6 },
        { "Name": "Longsword", "Cost": 40, "Damage": 7 },
        { "Name": "Greataxe", "Cost": 74, "Damage": 8 },
        ]
armors = [
        { "Name": "None", "Cost": 0, "Armor":       0 },
        { "Name": "Leather", "Cost": 13, "Armor":       1 },
        { "Name": "Chainmail", "Cost": 31, "Armor":       2 },
        { "Name": "Splintmail", "Cost": 53, "Armor":       3 },
        { "Name": "Bandedmail", "Cost": 75, "Armor":       4 },
        { "Name": "Platemail", "Cost": 102, "Armor":       5 },
        ]
rings = [
        { "Name": "No Ring", "Cost": 0, "Damage": 0, "Armor": 0 },
        { "Name": "Damage +1", "Cost": 25, "Damage": 1, "Armor": 0 },
        { "Name": "Damage +2", "Cost": 50, "Damage": 2, "Armor": 0 },
        { "Name": "Damage +3", "Cost": 100, "Damage": 3, "Armor": 0 },
        { "Name": "Defense +1", "Cost": 20, "Damage": 0, "Armor": 1 },
        { "Name": "Defense +2", "Cost": 40, "Damage": 0, "Armor": 2 },
        { "Name": "Defense +3", "Cost": 80, "Damage": 0, "Armor": 3 },
        ]

def play(a, b, r):
    damage = max(a["Damage"] - b["Armor"], 1)
    b["Hit Points"] -= damage
    if b["Hit Points"] < 0:
        #print(b["Name"], "dies in round", r, b["Hit Points"], a["Hit Points"])
        return False
    return True

def game(player, boss):
    r = 1
    while True:
        if not play(player, boss, r):
            return True
        if not play(boss, player, r):
            return False
        r += 1

bestcost = 0
for weapon in weapons:
    print(weapon)
    for armor in armors:
        print(armor)
        for ring1 in rings:
            for ring2 in rings:
                if ring1 == ring2 and ring1['Name'] != "No Ring":
                    continue

                p = deepcopy(player)
                b = deepcopy(boss)
                p["Damage"] += weapon["Damage"] + ring1["Damage"] + ring2["Damage"]
                p["Armor"] += armor["Armor"] + ring1["Armor"] + ring2["Armor"]
                cost = weapon["Cost"] + armor["Cost"] + ring1["Cost"] + ring2["Cost"]
                if not game(p, b):
                    if cost >= bestcost:
                        print(p, 'versus', b, weapon["Name"], armor["Name"], ring1["Name"], ring2["Name"], cost)
                        bestcost = cost
