n = int(input())
op = -1
output = 0
""" Initial shitty solution
for i in range(1,n+1):
    i *= op
    output += i
    op *= -1

print(output)
"""

if n == 1:
    print(-1)
else:
    if n % 2 == 0:
        print(n//2)
    else:
        print(((n//2)+1)*-1)


