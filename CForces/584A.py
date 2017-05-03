n, t = [int(x) for x in input().split(' ')]
a = True

for i in range(10**(n-1),10**n):
    if i % t == 0:
        a = False
        print(i)
        break
if a:
    print(-1)
