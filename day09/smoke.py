#!/usr/bin/env python3

with open("test", "r") as f:
    data = list(map(lambda x: list(map(int, x.strip())), f.readlines()))

def prev_neighbors(x,y):
    if x > 0:
        yield x - 1, y
    if y > 0:
        yield x, y - 1

def next_neighbors(x,y):
    if x < len(data[0]) - 1:
        yield x + 1, y
    if y < len(data) - 1:
        yield x, y + 1

basins = []

point_to_basin = {}

s = 0
for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == 9:
            continue
        for nx, ny in prev_neighbors(x, y):
            print(x,y, nx,ny, data[y][x], data[ny][nx])
            if (data[y][x] >= data[ny][nx] or True) and data[ny][nx] != 9:
                basins[point_to_basin[(nx, ny)]] += 1
                point_to_basin[(x,y)] = point_to_basin[(nx, ny)]
        #for nx, ny in next_neighbors(x, y):
        if (data[y][x] < data[ny][nx] or True) and (x, y) not in point_to_basin.keys():
            basins.append(1)
            point_to_basin[(x,y)] = len(basins) - 1
        else:
            s += data[y][x] + 1

basins.sort(reverse=True)

print(basins, point_to_basin)
