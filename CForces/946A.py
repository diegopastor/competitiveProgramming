n = int(input())
a = [int(x) for x in input().split(' ')]
b = [x for x in a if x < 0]
c = [x for x in a if x > 0]
print(sum(c)+abs(sum(b)))
