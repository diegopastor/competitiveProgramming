n = input()
m = input() 
a = []

for i in range(len(n)):
    a.append(int(n[i])^int(m[i]))

a = [str(x) for x in a]
print(''.join(a))
