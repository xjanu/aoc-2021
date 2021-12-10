#!/usr/bin/env python3

with open("test", "r") as f:
    data = list(map(lambda x: list(map(int, x.strip())), f.readlines()))

def neighbors(x,y):
    if x > 0:
        yield x - 1, y
    if x < len(data[0]) - 1:
        yield x + 1, y
    if y > 0:
        yield x, y - 1
    if y < len(data) - 1:
        yield x, y + 1

s = 0
for y in range(len(data)):
    for x in range(len(data[0])):
        for nx, ny in neighbors(x, y):
            if data[y][x] >= data[ny][nx]:
                break
        else:
            s += data[y][x] + 1

print(s)
