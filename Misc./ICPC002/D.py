from sys import stdin
from collections import namedtuple, deque

inf = float('inf')
Edge = namedtuple('Edge','start, end, cost')

for line in stdin:
    edges = []
    n,m = map(int,line.split(' '))
    for i in range(m):
        a,b,c = map(int,input().split(' '))
        edges.append(Edge(a,b,c))
    vertices = set(sum(([e.start, e.end] for e in edges),[]))

    print(edges)
    print(vertices)

