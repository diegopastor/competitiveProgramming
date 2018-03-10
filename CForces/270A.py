t = int(input())
for i in range(t):
    deg = int(input())
    if(360 % (180-deg) == 0):
        print('YES')
    else:
        print('NO')


