import pandas as pd

file1 = open('input/4.txt', 'r')
lines = file1.readlines()

total = 0
total2 = 0

for line in lines:

    line = line.strip()
    nums = line.split(",")
    nums = [x.split("-") for x in nums]

    nums = [[int(x[0]), int(x[1])] for x in nums]

    if nums[0][0] <= nums[1][0] and nums[0][1] >= nums[1][1]:
        total += 1
    elif nums[1][0] <= nums[0][0] and nums[1][1] >= nums[0][1]:
        total +=1

    if nums[0][0] <= nums[1][1] and nums[0][1] >= nums[1][0]:
        total2 += 1
    elif nums[1][0] <= nums[0][1] and nums[1][1] >= nums[0][0]:
        total2 +=1

print(total)
print(total2)