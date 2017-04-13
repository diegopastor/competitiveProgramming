from math import gcd

s, ns, n = [int(x) for x in input().split(' ')]

while True:
    if n - gcd(s,n) >= 0:
        n -= gcd(s,n)
    else:
        print(1)
        break
    if n - gcd(ns,n) >= 0:
        n-= gcd(ns,n)
    else:
        print(0)
        break
