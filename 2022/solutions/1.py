file1 = open('input/1.txt', 'r')
lines = file1.readlines()
count = 0
# Strips the newline character
x = []
total = 0
for line in lines:
    count = count+1
    if line.strip() == "":
        x.append(total)
        total = 0
    else:
        total = total + int(line)
x.sort(reverse=True)
print(max(x))
print(sum(x[0:3]))