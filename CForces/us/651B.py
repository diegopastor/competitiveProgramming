input()
pics = [int(x) for x in input().split(' ')]
ans = 0
maxs = []

if len(pics) == len(set(pics)):
    print(len(pics)-1)
else:
    for pic in pics:
        maxs += [pics.count(pic)]
    print(max(maxs))
