n = int(input())
m = 1
nms = ["Sheldon","Leonard","Penny","Rajesh","Howard"]

while (m*5) < n:
    n -= m * 5
    m *= 2

print(nms[(n-1)//m])
