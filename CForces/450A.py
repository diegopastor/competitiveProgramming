n,m = [int(x) for x in input().split(' ')]
q = [int(x) for x in input().split(' ')]
c = []
for i in range(n):
    c.append([i+1,q[i]])

while(len(c) > 1):
    if c[0][1] - m <= 0:
        c.pop(0)
    else:
        c[0][1] -= m
        temp = c.pop(0)
        c.append(temp)

print(c[0][0])
