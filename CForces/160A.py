input()
coins = list(input().split(' '))
coins = [int(c) for c in coins]
coins = sorted(coins)
coins = coins[::-1]
sumB = sum(coins)
sumA = 0
i = 0
while sumA <= sumB:
    sumA += coins[i]
    sumB -= coins[i]
    i += 1
    
print(i)

