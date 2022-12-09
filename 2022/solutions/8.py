from collections import deque


file1 = open('input/8.txt', 'r')
lines = file1.readlines()
lines = [line.strip() for line in lines]

trees = []
covered = []
views = []
for line in lines:
    trees.append([int(x) for x in line])
    covered.append([0 for x in line])
    views.append([1 for x in line])


for i in range(0,len(trees)):
    l = len(line)
    for round, r in enumerate([range(0,l), reversed(range(0,l))]):
        tallest1 = -1
        for j in r:
            if trees[i][j] > tallest1:
                tallest1 = trees[i][j]
                covered[i][j] = 1

for j in range(0,len(trees[0])):
    l = len(trees)
    for round, r in enumerate([range(0,l), reversed(range(0,l))]):
        tallest1 = -1
        for i in r:
            if trees[i][j] > tallest1:
                tallest1 = trees[i][j]
                covered[i][j] = 1

leny = len(trees) 
lenx = len(trees[0])
for y in range(1,len(trees)-1):
    for x in range(1,len(trees[0])-1):
        cur = trees[y][x]
        for i in range(y+1,leny):
            if trees[i][x] >= cur or i == leny-1:
                views[y][x] = views[y][x] * abs(i - y)
                break
        for i in reversed(range(0,y)):
            if trees[i][x] >= cur or i == 0:
                views[y][x] = views[y][x] * abs(i - y)
                break

        for j in range(x+1,lenx):
            if trees[y][j] >= cur or j==lenx-1:
                views[y][x] = views[y][x] * abs(j - x)
                break
        for j in reversed(range(0,x)):
            if trees[y][j] >= cur or j==0:
                views[y][x] = views[y][x] * abs(j - x)
                break
            

print( sum(  [sum(x) for x in covered]  ))
print( max(  [max(x) for x in views]  ))

