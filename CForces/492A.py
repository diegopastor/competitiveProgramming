n = int(input())
con = 0
i = 0
while con <= n:
    i += 1
    con += (i*(i+1))//2
print(i-1)

