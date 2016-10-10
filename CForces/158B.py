input()
groups = list(input().split(' '))
groups = [int(group) for group in groups]
taxis = 0
g3 = 0
g2 = 0
g1 = 0
for group in groups:
    if group == 4:
        taxis += 1
    elif group == 3:
        g3 += 1
        taxis += 1
    elif group == 2:
        g2 += 1
    elif group == 1:
        g1 += 1

taxis += g2//2

if g2 % 2 != 0:
    taxis += 1

if g3 < g1:
    g1 -= g3
    if g2 % 2 != 0:
        g1 -= 2
    if g1 > 0:
        taxis += g1 // 4
        if g1 % 4 != 0:
            taxis += 1

print(taxis)
