n = int(input())
a = [int(x) for x in input().split(' ')]
b = 0
for num in a:
    if num < 0:
        b -= num
        a.pop(num)

print(sum(a)+b)
