from math import log10 as log
from math import ceil
t = int(input())

l2 = log(2)
l5 = log(5)

for i in range(t):
    a,b = map(int,input().split(' '))
    if a == b:
        print(a+1)
    else:
        ans = (a * l2) + (b * l5)
        print(ceil(ans))
