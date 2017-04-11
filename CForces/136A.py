n = int(input())
gifts = [int(x) for x in input().split(' ')]
ans = [0]*len(gifts)

for i in range(len(gifts)):
    ans[gifts[i]-1] = i+1

print(' '.join([str(x) for x in ans]))
