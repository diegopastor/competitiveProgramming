from collections import deque

r, c = [int(i) for i in input().split(' ')]
g = {}

dX = [-1, 0, 1, 0]
dY = [0, 1, 0, -1]

for x in range(r):
    row = [i for i in input() if i != ' ']
    y = 0
    # Each node of the graph points to a 2-tuple representing:(visited?/distance, # of trainers)
    # We reverse the Start and End nodes to avoid calculating BFS again for each trainer since the
    # main trainer's distance wont change BFS(s,e) == BFS(e,s)
    for col in row:
        if col == 'S':
            exitNode = (x,y)
            g[exitNode] = (-1, 0)
        elif col == 'E':
            startNode = (x,y)
            g[startNode] = (0, 0)
        elif col != 'T':
            g[(x,y)] = (-1, int(col))
        y += 1

#BFS
q = deque([startNode])
while q:
    c = q.popleft()
    for i in range(4):
        neighbour = (c[0] + dX[i], c[1] + dY[i])
        if neighbour in g and g[neighbour][0] == -1:
            q.append(neighbour)
            g[neighbour] = (g[c][0] + 1, g[neighbour][1])

escapeIn = g[exitNode][0]

def inRange(graph):
    t = 0
    for node in graph: 
        if graph[node][0] != -1 and graph[node][0] <= escapeIn:
            t += graph[node][1]
    return t

print(inRange(g))
