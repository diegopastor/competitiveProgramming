nXm = list(input().split(' '))
n = int(nXm[0])
m = int(nXm[1])
if (n * m) % 2 == 0:
    print((n*m)//2)
else:
    print(((n*m)-1)//2)
