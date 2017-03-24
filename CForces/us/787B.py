n,m = [int(x) for x in input().split(' ')]
groups = dict()

for i in range(m):
    group = input().split(' ')
    groups[group[0]] = group[1:]


print(groups)
