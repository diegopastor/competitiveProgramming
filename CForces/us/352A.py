n = int(input())
cards = [int(x) for x in input().split(' ')]
fives = cards.count(5)
ceros = cards.count(0)

def closest(n):
    if n < 9:
        return 0
    if n % 9 == 0:
        return n
    else:
        for i in range(n,0,-1):
            if i % 9 == 0:
                return i
if ceros == 0:
    print(-1)
elif fives < 9:
    print(0)
else:
    print('5'*closest(n)+'0'*ceros)
