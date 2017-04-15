n,m,a,b = [int(x) for x in input().split(' ')]

if m*a > b:
    cost = (n % m) * a
    if cost > b:
        print(n//m * b+b)
    else:
        print(n//m * b + cost)
else:
    print(n*a)
