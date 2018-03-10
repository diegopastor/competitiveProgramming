from math import sqrt
a,b,c = [int(x) for x in input().split(' ')]
x = sqrt((a*c/b))
y = sqrt((a*b/c))
z = sqrt((b*c/a))

print(int(4*(x+y+z)))
