from collections import deque

"""
199D - Jumping on Walls
"""

l, j = [int(i) for i in input().split(' ')]
wallA = list(input())
wallB = list(input())
g = {}

for i in range(l):
    # Each 4-tuple represents: (Visited?, Current Height, Current Water Height, Drowned?)
    if wallA[i] == '-':
        g[(1,i+1)] = (-1, 0, 0, False) 
    if wallB[i] == '-':
        g[(-1,i+1)] = (-1, 0, 0, False)

g[(1, 1)] = ('VISITED', 1, 0, False)
q = deque([(1, 1)]) 

while q:
    c = q.popleft()
    up = (c[0], c[1]+1)
    down = (c[0], c[1]-1)
    jump = (c[0]*-1, c[1] + j)
    if g[c][1] <= g[c][2]: 
        g[c] = (g[c][0], g[c][1], g[c][2], True)
    if up in g and g[up][0] == -1:
        q.append(up)
        g[up] = ('VISITED', g[c][1] + 1, g[c][2] + 1, g[c][3])
    if down in g and g[down][0] == -1:
        q.append(down)
        g[down] = ('VISITED', g[c][1] - 1, g[c][2] + 1, g[c][3])
    if jump in g and g[jump][0] == -1:
        q.append(jump)
        g[jump] = ('VISITED', g[c][1] + j, g[c][2] + 1, g[c][3])

def graphHasEscape(graph):
    for node in graph:
        result = graph[node]
        if result[0] == 'VISITED' and ((result[1] + 1 > l) or (result[1] + j > l)) and not result[3]:
            return True
            break
    return False

if graphHasEscape(g):
    print('YES')
else:
    print('NO')
