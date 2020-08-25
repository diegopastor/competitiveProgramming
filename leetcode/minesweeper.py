from collections import deque

nX = [1,1,0,-1,-1,-1,0,1]
nY = [0,-1,-1,-1,0,1,1,1]

def minesweep(board, click):
    g = {}
    for x in range(len(board)):
        for y in range(len(board[x])):
            g[(x,y)] = board[x][y]

    if g[(click[0], click[1])] == 'M':
        board[click[0]][click[1]] = 'X'
        return board

    q = deque([(click[0], click[1])])
    visited = []
    while q: 
        c = q.popleft()
        if c not in visited:
            visited.append(c)
            if g[c] == 'E':
                adjMines = 0
                for i in range(8):
                    n = (c[0] + nX[i], c[1] + nY[i])
                    if n in g and g[n] == 'M':
                        adjMines += 1

                for i in range(8):
                    n = (c[0] + nX[i], c[1] + nY[i])
                    if n in g and g[n] == 'E' and adjMines == 0:
                        q.append(n)
                        
                adjMines = 'B' if adjMines == 0 else str(adjMines)
                board[c[0]][c[1]] = adjMines

    return board

print(minesweep([['E', 'E', 'E', 'E', 'E'],
                 ['E', 'E', 'M', 'E', 'E'],
                 ['E', 'E', 'E', 'E', 'E'],
                 ['E', 'E', 'E', 'E', 'E']],
                 [3,0]))
