a, b = [int(x) for x in input().split(' ')]
h = min(a,b)
n = (max(a,b) - min(a,b)) // 2

print(h,n)

