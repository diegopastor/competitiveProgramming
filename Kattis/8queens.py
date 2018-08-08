import sys

board = []
queens = []
ans = 'valid'

def generateDiagonals(point):
    diagonals = []
    #For ++ diagonal
    x, y = point[0], point[1]
    while x < 7 and y < 7:
        x += 1
        y += 1
        diagonals.append([x,y])
    #For -- diagonal
    x, y = point[0], point[1]
    while x > 0 and y > 0:
        x -= 1
        y -= 1
        diagonals.append([x,y])
    #For +- diagonal
    x, y = point[0], point[1]
    while x < 7 and y > 0:
        x += 1
        y -= 1
        diagonals.append([x,y])
    #For -+ diagonal
    x, y = point[0], point[1]
    while x > 0 and y < 7:
        x -= 1
        y += 1
        diagonals.append([x,y])
    return diagonals

for line in sys.stdin:
    board.append(list(line)[:-1])

for x in range(8):
    for y in range(8):
        if board[x][y] == '*':
            queens.append([x,y])

xs = [x for x,y in queens]
ys = [y for x,y in queens]

if len(set(xs)) < 8 or len(set(ys)) < 8:
    ans = 'invalid'

diagonals = []

for queen in queens:
    diagonals.extend(generateDiagonals(queen))

for queen in queens:
    if queen in diagonals:
        ans = 'invalid'

print(ans)
