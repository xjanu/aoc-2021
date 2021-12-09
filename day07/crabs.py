#!/usr/bin/env python3

# read
with open("input", "r") as f:
    data = list(map(int, f.read().split(",")))

#data = [16,1,2,0,4,2,7,1,2,14]

total = []
for i in range(min(data), max(data)+1):
    fuel = 0
    for crab in data:
        n = abs(crab-i)
        fuel += n*(n+1) // 2
    total.append((fuel, i))

print(sorted(total)[0])
