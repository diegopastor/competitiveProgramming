n = int(input())
start = input()[1]
swaps = 1

for i in range(n-1):
    if input()[1] != start:
        if start == '0':
            start = '1'
        else:
            start = '0'
        swaps += 1    
    
print(swaps)
