t = int(input())
for i in range(t):
    print("Case "+str(i+1)+": "+str(max([int(x) for x in input().split(' ')])))
