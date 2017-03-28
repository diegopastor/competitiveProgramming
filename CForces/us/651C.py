c = int(input())
pos = dict()
heros = [] 

tups = []

for case in range(c):
    heros.append([int(i) for i in input().split(' ')])

for a in range(len(heros)):
    for b in range(a+1,len(heros)-1):
        tups.append([(abs(heros[a][0] - heros[b][0]) + abs(heros[a][1] - heros[b][1])), int((((heros[a][0] - heros[b][0])**2) + ((heros[a][1] - heros[b][1])**2))**.5)])

ans = 0
for tup in tups:
    if tup[0] == tup[1]:
        ans += 1
print(tups)
print(ans)
