tsq = input().split(' ')
t=int(tsq[0])
s=int(tsq[1])
q=int(tsq[2])
ans = 0
#
while s < t:
    ans += 1
    s *= q

print(ans)
