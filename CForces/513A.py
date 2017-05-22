x,y,m,n = [int(x) for x in input().split(' ')]
if x != y:
    if x == max(x,y):
        print('First')
    else:
        print('Second')
else:
    print('Second')
