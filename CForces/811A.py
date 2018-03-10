a, b = [int(x) for x in input().split(' ')]
turn = True
c = 1

while(True):
    if(turn):
        if(a - c >= 0):
            a -= c
            turn = False
        else:
            print('Vladik')
            break
    else:
        if(b - c >= 0):
            b -= c
            turn = True
        else:
            print('Valera')
            break
    c += 1


