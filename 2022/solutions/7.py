from collections import deque


file1 = open('input/7.txt', 'r')
lines = file1.readlines()
lines = [line.strip() for line in lines]

result = {}
dir = []
x = 0 
for line in lines:
    if line.startswith('$ cd ..'):
        dir.pop()
    elif line.startswith('$ cd'):
        folder = line.split(" ")[2]
        dir.append(folder)
        str_dir = " ".join(dir)
        if str_dir not in result:
            result[str_dir] = 0
    elif line.startswith('$') or line.startswith('ls') or line.startswith('dir'):
        continue
    else:
        size = line.split(" ")[0]
        str_dir = " ".join(dir)
        result[str_dir] += int(size)

total = 0

final = {}
for i in result:
    int_total = 0
    for j in result:
        if j[0:len(i)] == i:
            int_total += result[j]
    
    final[i] = int_total

print(sum([final[i] for i in final if final[i] <= 100000]))

reduction = 30000000 - (70000000 - final["/"])
print(min(([final[i] for i in final if final[i] >= reduction])))

