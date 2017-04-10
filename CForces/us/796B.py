n,m,k = [int(x) for x in input().split(' ')]
holes = [int(x) for x in input().split(' ')]

bonePos = 1
table = [0]*n

for hole in holes:
    table[hole-1] = 1

if table[0] != 1:
    for i in range(k):
        swap = [int(x) for x in input().split(' ')]
        if table[swap[1]-1] == 1: 
            bonePos = swap[1]
            break
        else:
            bonePos = swap[1]

print(bonePos)
