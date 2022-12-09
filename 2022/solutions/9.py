
def move(h,t):
    if not (abs(h[0] - t[0]) <=1 and abs(h[1] - t[1]) <= 1):
        xstep = 0
        ystep = 0
        if h[0] > t[0]:
            xstep += 1
        if h[0] < t[0]:
            xstep -= 1
        if h[1] > t[1]:
            ystep += 1
        if h[1] < t[1]:
            ystep -= 1

        t[0] += xstep
        t[1] += ystep
    return t

def run(lines, rope_len):
    visited = set()
    visited.add((0,0))
    coords = [[0,0] for x in range(0,rope_len)]

    for line in lines:
        line = line.split(" ")
        dir = line[0]
        steps = int(line[1])
        for _ in range(steps):
            if dir == 'R': 
                coords[0][0] += 1       
            elif dir == 'L': 
                coords[0][0] -= 1
            elif dir == 'U': 
                coords[0][1] += 1
            elif dir == 'D': 
                coords[0][1] -= 1
            
            for i in range(1, rope_len):
                coords[i] = move(coords[i-1], coords[i])
            
            visited.add(tuple(coords[rope_len-1]))

    return(len(visited))

file1 = open('input/9.txt', 'r')
lines = file1.readlines()
lines = [line.strip() for line in lines]

print(run(lines, 2))
print(run(lines, 10))