#!/usr/bin/python3

import re

food = []
ingredients = set()
allergens = set()

with open('21.txt') as f:
    for line in f:
        m = re.match('(.*) \(contains (.*)\)', line)
        i = set(m[1].split())
        ingredients |= i
        a = set(m[2].split(', '))
        allergens |= a
        food.append((i, a))

print('ingredients:', ingredients)
print('allergens:', allergens)
#print('food:', food)

non_allergens = ingredients.copy()
allergen_candidates = {}

for a in sorted(allergens):
    diff = ingredients.copy()
    #union = set()
    for f in [x[0] for x in food if a in x[1]]:
        diff &= f
        #union |= f
    print(a, 'is one of', diff)
    allergen_candidates[a] = diff
    non_allergens -= diff

print('non-allergens:', non_allergens)

number_of_non_allergens = 0
for i in [x[0] for x in food]:
    for ii in i:
        if ii in non_allergens:
            number_of_non_allergens += 1
print('21a:', number_of_non_allergens)

allergen_food = {}
while len(allergen_candidates) > 0:
    for a in allergen_candidates:
        if len(allergen_candidates[a]) == 1:
            break
    else:
        raise
    i = allergen_candidates[a].pop()
    allergen_food[a] = i
    print(a, 'is', i)
    del allergen_candidates[a]
    for x in allergen_candidates:
        allergen_candidates[x].discard(i)

print('21b:', ",".join([allergen_food[x] for x in sorted(allergen_food.keys())]))
