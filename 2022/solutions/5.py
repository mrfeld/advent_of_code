import pandas as pd
import copy

file1 = open('input/5.1.txt', 'r')
file2 = open('input/5.2.txt', 'r')

lines = file1.readlines()
lines2 = file2.readlines()

lines = [x.rstrip('\n') for x in lines]
lines2 = [x.rstrip('\n') for x in lines2]
l = int((len(lines[0]) + 1) / 4)

moves = []
stacks = []
for x in range(l):
    stacks.append([])

for line in lines:
    x = 0
    start = 0
    end = 0
    while x < l:
        start = x*4+1
        end = x*4+2
        crate = line[start:end]
        if crate != ' ':
            stacks[x].append(crate)
        x+=1
        
for x in stacks:
    x.reverse()

for line in lines2:
    line = line.split(' ')
    move = [int(line[1]), int(line[3]),int(line[5])]
    moves.append(move)

for i in [1,2]:
    stacks2 = copy.deepcopy(stacks)

    for move in moves:
        num = move[0]
        f = move[1] - 1
        t = move[2] - 1
        moving = []
        for x in range(num):
            moving.append(stacks2[f].pop())
        
        if i==2:
            moving.reverse()
            
        stacks2[t].extend(moving)
    
    print(''.join([x[-1] for x in stacks2]))