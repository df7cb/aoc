#!/usr/bin/python3

import re

path = ['/']
files = {'/': {}}

def walk_path(files, path):
    for entry in path:
        files = files[entry]
    return files

with open("07.txt") as f:
    for line in f:
        #print(line.strip())
        if m := re.match('^\$ cd (.*)', line):
            name = m.group(1)
            if name == '/':
                path = ['/']
            elif name == '..':
                path.pop()
            else:
                path.append(name)
            #print(path)
            this_dir = walk_path(files, path)
        elif m := re.match('^\$ ls', line):
            pass
        elif m := re.match('^dir (.*)', line):
            this_dir[m.group(1)] = {}
        elif m := re.match('^(\d+) (.*)', line):
            this_dir[m.group(2)] = int(m.group(1))
        else:
            assert(0)
        #print(this_dir)

dir_sizes = []

def walk_tree(files):
    s = 0
    for file in files:
        cont = files[file]
        if isinstance(cont, dict):
            s += walk_tree(cont)
        elif isinstance(cont, int):
            s += cont
        else:
            assert(0)

    dir_sizes.append(s)

    return s

disk_size = 70000000
need_size = 30000000
total_size = walk_tree(files)
min_delete = total_size - (disk_size - need_size)

print(total_size)
print("need to delete at least", min_delete)

delete = [x for x in dir_sizes if x >= min_delete][0]
print("delete", delete)
