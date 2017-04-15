n, m = [int(x) for x in input().split(' ')]

alt = True
right = True

for i in range(n):
    if alt:
        print('#'*m)
        alt = False
    else:
        if right:
            print(('.'*(m - 1)) + ('#'))
            right = False
        else:
            print(('#')+('.' * (m-1)))
            right = True
        alt = True
