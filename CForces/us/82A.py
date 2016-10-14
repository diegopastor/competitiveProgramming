n = int(input())
n = n-1
queue = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']

def extendQ(q,n):
    for i in range(0,n):
        q.append(q[i])
        q.append(q[i])
    return q

ans = extendQ(queue,n)
print(ans[n])

