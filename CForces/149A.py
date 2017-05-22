k = int(input())
months = sorted([int(x) for x in input().split(' ')])[::-1]
days = 0
m = k
s = 0
while k > 0:
    if months: 
        k -= months[0]
        s += months[0]
        months = months[1:]
        days += 1
    else:
        break

if s >= m:
    print(days)
else:
    print(-1)

