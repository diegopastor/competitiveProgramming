a, b = [int(x) for x in input().split(' ')]
c, d = [int(x) for x in input().split(' ')]


if a % 2 == 0 and b % 2 != 0 and c % 2 == 0 and d % 2 == 0 or a % 2 == 0 and b % 2 == 0 and c % 2 == 0 and d % 2 != 0:
    print(-1)
else:
    i = 0
    j = 0
    while True:
        if (b + a*i) < (d + c*j):
            i += 1
        elif (d + c*j) < (b + a*i):
            j += 1
        else:
            print(d+c*j)
            break
