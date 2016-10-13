num = int(input())

def isLucky(n):
    c = 0 
    for digit in str(n):
        if digit == '4' or digit == '7':
            c += 1
    if len(str(n)) == c:
        return True
    else:
        return False

luckyNumbers = [x for x in range(1,1001) if isLucky(x)]

for n in luckyNumbers:
    if num % n == 0:
        ans = True
        break 
    else: 
        ans = False
if ans:
    print('YES')
else:
    print('NO')
