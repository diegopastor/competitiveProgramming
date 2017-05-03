n = int(input())
contests = [int(x) for x in input().split(' ')][::-1]
ans = 0

for i in range(len(contests)):
    for j in range(len(contests[i:])):


print(ans)
