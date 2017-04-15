s, n = [int(x) for x in input().split(' ')]

dragons = []

for i in range(n):
    dragons.append([int(x) for x in input().split(' ')])

dragons.sort(key = lambda x: x[0])

def find_dragon(l):
    best_drag = [999999999,0]
    for dragon in l:
        if dragon[0] <= best_drag[0] and dragon[1] >= best_drag[1]:
            best_drag = [dragon[0],dragon[1]]
    return best_drag

kills = 0
for i in range(n):
    ans = find_dragon(dragons)
    if ans[0] < s:
        kills += 1
        s += ans[1]
        dragons.pop(dragons.index([ans[0],ans[1]]))

if kills == n:
    print('YES')
else:
    print('NO')
