import pandas as pd
import string

letters = string.ascii_letters

file1 = open('input/3.txt', 'r')
lines = file1.readlines()

total = 0
total2 = 0 
sacks = []
for line in lines:
    line = line.strip()
    
    l = len(line)
    l2 = int(l/2)
    result = list(set(line[0:l2]).intersection(set(line[l2:l])))[0]
    total = total + letters.index(result) + 1

    sacks.append(line)
    if len(sacks) == 3:
        result = list(set(sacks[0]).intersection(set(sacks[1])).intersection(set(sacks[2])))[0]
        total2 = total2 + letters.index(result) + 1
        sacks = []

print(total)
print(total2)