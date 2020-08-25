from collections import deque
from random import choice


nX = [1, 0, -1, 0]
nY = [0, 1, 0, -1]

def islands(grid):
    g = {}
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == "1":
                g[(x,y)] = -1

    islands = 0
    unvisited = set([k for k, v in g.items() if v == -1])
    while unvisited:
        islands += 1
        q = deque([choice(list(unvisited))])
        while q:
            c = q.popleft()
            g[c] = 1
            for i in range(4):
                neighbour = (c[0] + nX[i], c[1] + nY[i])
                if neighbour in g and g[neighbour] == -1:
                    g[neighbour] = 1
                    q.append(neighbour)

        unvisited = set([k for k, v in g.items() if v == -1])

    return islands

print(islands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
])) # Expected 1
print(islands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
])) # Expected 3
