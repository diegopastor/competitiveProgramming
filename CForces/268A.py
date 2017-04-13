n = int(input())
ans = 0
a = []
b = []

for i in range(n):
    x, y = [int(x) for x in input().split(' ')]
    a.append(x)
    b.append(y)

for el in a:
    ans += b.count(el)

print(ans)
