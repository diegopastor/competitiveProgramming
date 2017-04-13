n, m = [int(x) for x in input().split(' ')]

days = 0
buy = 0
while n:
    n -= 1
    days += 1
    buy += 1
    if buy == m: 
        n += 1
        buy = 0

print(days)
