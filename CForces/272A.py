n = int(input()) + 1
f = sum([int(x) for x in input().split(' ')])
print(sum(1 for y in range(f + 1, f + 6) if y % n != 1))
