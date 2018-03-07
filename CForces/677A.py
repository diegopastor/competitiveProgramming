n, h = [int(x) for x in input().split(' ')]
p = [int(x) for x in input().split(' ')]
print(n + sum(i > h for i in p))
