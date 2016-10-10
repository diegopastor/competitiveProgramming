l1 = list(input().split(' '))
l2 = list(input().split(' '))
c = 0
m = l1[1]
n = l2[int(m)-1]

for score in l2:
    if int(score) >= int(n):
        if int(score) == 0:
            c = c
        else:     
            c = c + 1
print(c)
