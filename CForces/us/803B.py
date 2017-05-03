n = int(input())
a = [int(x) for x in input().split(' ')]
ceros = []

for i in range(n):
    if a[i] == 0:
        ceros.append(i)

mins = [str(min([abs(x-y) for y in ceros])) for x in range(len(a))]
print(' '.join(mins))
