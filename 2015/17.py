#!/usr/bin/python3

containers = []

with open('17.txt') as f:
    for line in f:
        containers.append(int(line))

containers.sort()

print(containers)

count = 0
container_number = len(containers)
container_number_count = 0

def fill(used_containers, containers, left):
    if left < 0:
        return
    elif left == 0:
        print(used_containers)
        global count, container_number, container_number_count
        count += 1
        if len(used_containers) < container_number:
            container_number = len(used_containers)
            container_number_count = 0
        if len(used_containers) == container_number:
            container_number_count += 1
        return
    for p in range(len(containers)):
        if containers[p] > left:
            break
        fill(used_containers + [containers[p]], containers[p+1:], left - containers[p])

fill([], containers, 150)
print(count, container_number, container_number_count)
