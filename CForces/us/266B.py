n,t = [int(x) for x in input().split(' ')]
q = input()
q = [c for c in q]

for i in range(t):
    if q[i] == 'B' and q[i+1] == 'G':
        q[i], q[i+1] = q[i+1],q[i]

print(q)
