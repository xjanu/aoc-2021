#!/usr/bin/env python3

from math import prod

with open("input", "r") as f:
    data = list(map(lambda x: list(map(int, x.strip())), f.readlines()))

def prev_neighbors(x,y):
    if x > 0:
        yield x - 1, y
    if y > 0:
        yield x, y - 1

basins = [[(x, y)] for x in range(len(data[0])) for y in  range(len(data))]

def find_basin(x, y):
    for i in range(len(basins)):
        if (x, y) in basins[i]:
            return i

for x in range(len(data[0])):
    for y in range(len(data)):
        if data[y][x] == 9:
            basins.remove([(x, y)])
            continue
        for nx, ny in prev_neighbors(x, y):
            if data[ny][nx] == 9:
                continue
            b_1 = find_basin(x, y)
            b_2 = find_basin(nx, ny)
            if b_1 == b_2:
                continue
            basins[b_1].extend(basins[b_2])
            basins.pop(b_2)

basins = list(map(len, basins))
basins.sort(reverse=True)

print(basins[:3], prod(basins[:3]))
