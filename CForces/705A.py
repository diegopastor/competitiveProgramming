n = int(input())
f = True
s = 'I hate '
for i in range(n - 1):
    if f: 
        s += 'that I love '
        f = False
    else:
        s += 'that I hate '
        f = True
s += 'it' 
print(s)
