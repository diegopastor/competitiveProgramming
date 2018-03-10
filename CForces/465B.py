n = int(input())
m = [int(x) for x in input().split(' ')]
ans = sum(m)

m = m[::-1]
if(ans > 0):
    m = m[m.index(1):]
m = m[::-1]

for i in range(len(m)):
    if(i == 0):
        curr = m[i]
        past = m[i]
    else:
        curr = m[i]
    if(past == 1 and curr == 0):
        ans += 1
    past = m[i] 

print(ans)
