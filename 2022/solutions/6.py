from collections import deque


file1 = open('input/6.txt', 'r')
line = file1.readlines()[0]

for r in [4,14]:
    chars = deque(r*[line[0]], r)

    count = 0
    for x in line:
        count += 1
        chars.pop()
        chars.appendleft(x)
        if( len(set(chars)) == r):
            break

    print(count)
