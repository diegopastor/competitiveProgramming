import sys
n = int(input())
points = []

for line in sys.stdin:
    line = line.split(' ')
    points += [[int(line[0]),int(line[1])]]

print(points)

