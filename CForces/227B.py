input()
a = list(map(int,input().split(' ')))
l = len(a)
input()
q = list(map(int,input().split(' ')))

pos = {n:i+1 for (n,i) in zip(a,range(l))}

v = 0
p = 0

for query in q:
    v += pos[query]
    p += l - (pos[query] -1)

print(v,p)
