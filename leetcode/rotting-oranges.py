from collections import deque

def minMinutes(grid):
    minutes = 0
    fresh = {}
    rotten = {}
    dX = [-1, 0, 1, 0]
    dY = [0, 1, 0, -1]
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == 1:
                fresh[(x,y)] = 1
            elif grid[x][y] == 2:
                rotten[(x,y)] = 1
    while len(fresh) > 0:
        minutes += 1
        infected = []
        for r in rotten:
            for i in range(4):
                neighbour = (r[0] + dX[i], r[1] + dY[i])
                if neighbour in fresh:
                    del fresh[neighbour]
                    infected.append(neighbour)
        for i in infected:
            rotten[i] = 1
        if len(infected) == 0:
            return -1
    return minutes

# t1 = [[2,1,1],[1,1,0],[0,1,1]]
# t1 = [[2,1,1],[0,1,1],[1,0,1]]
# t1 = [[2,1,0,2,1], [1,0,1,2,1], [1,0,0,2,1]]
print(minMinutes(t1))
