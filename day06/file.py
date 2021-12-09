#!/usr/bin/env python3

# read
with open("input", "r") as f:
    data = list(map(int, f.read().split(",")))

#data = [3,4,3,1,2]

nums = [data.count(i) for  i in range(9)]
print(nums)

def step(nums):
    new = nums.copy()
    for i in range(6):
        new[i] = nums[i+1]
    new[6] = nums[7] + nums[0]
    new[7] = nums[8]
    new[8] = nums[0]
    return new

for i in range(256):
    nums = step(nums)
    print(i, sum(nums))
