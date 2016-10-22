levels = int(input())
x = list(map(int,input().split(' ')))
x = x[1:]
y = list(map(int,input().split(' ')))
y = y[1:]
levels = [x for x in range(1,levels+1)]

if 0 in x:
    x = []

if 0 in y:
    y = []

if list(set(x + y)) == levels:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')
