n, t = [int(x) for x in input().split(' ')]
world = [int(x) for x in input().split(' ')]

v = 0

while v < t - 1:
    v = world[v] + v

if v == t-1:
    print('YES')
else:
    print('NO')
