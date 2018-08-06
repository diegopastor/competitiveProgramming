n, m = [int(x) for x in input().split(' ')]
plane = [i for i in range(1,m+1)]
segments = []
for i in range(n):
    lb,up = [int(x) for x in input().split(' ')]
    for j in range(lb,up+1):
        segments.append(j)

ans = list(set(plane) - set(segments))
print(len(ans))
if ans:
    print(*ans, sep=' ')
