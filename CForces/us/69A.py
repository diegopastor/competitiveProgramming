lines = int(input())
x = 0
y = 0
z = 0
for line in range(lines):
    xyz = input().split(' ')
    x += int(xyz[0])
    y += int(xyz[1])
    z += int(xyz[2])

if not x and not y and not z:
    print('YES')
else:
    print('NO')
