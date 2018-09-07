ups = [x=='U' for x in input()]
# A When you leave, always leave the seat up
# B When you leave, always leave the seat down
# C When you leave, always leave the seat as you would like to find it

# e.g. INPUT : 'UUUDUDU'
isUp = ups[0]
r = ups[0]
ups = ups[1:]
a,b,c, = 0,0,0

for seat in ups:
    if not isUp:
        a += 1
        seat = True
        isUp = True
    if not seat:
        a += 2

isUp = r

for seat in ups:
    if isUp:
        b += 1
        seat = False
        isUp = False
    if seat:
        b += 2

isUp = r

for seat in ups:
    if not seat and isUp or seat and not isUp:
        c += 1
        isUp = not isUp

print(a)
print(b)
print(c)
