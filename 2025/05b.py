#!/usr/bin/python3

import re
import psycopg

conn = psycopg.connect()
cur = conn.cursor()

fresh = []

with open("05.txt") as f:
    for line in f:
        if line == "\n": break

        m = re.match(r"(\d+)-(\d+)", line)
        fresh.append(f"[{m.group(1)},{m.group(2)}]")

const = "{" + ",".join(fresh) + "}"

cur.execute("select %s::int8multirange", [const])
res = cur.fetchone()

print(res)

num = 0

for r in res[0]:
    print(r)
    num += r.upper - r.lower

print(num)
