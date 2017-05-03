from itertools import groupby

input()
line = sorted([int(n) for n in input().split(' ')])
sums = {k:sum(list(g)) for (k, g) in groupby(line)}
print(sums)

