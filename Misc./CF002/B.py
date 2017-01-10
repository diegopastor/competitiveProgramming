seat = input()
s = seat[-1]
n = seat[:-1]
n = int(n)

if s == 'a':
    ss = 4
if s == 'b':
    ss = 5
if s == 'c':
    ss = 6
if s == 'd':
    ss = 3
if s == 'e':
    ss = 2
if s == 'f':
    ss = 1
    
iteration = n // 4
classA = [x+4 for x in range(-3,n+1,4)]
classB = [x+4 for x in range(-2,n+1,4)]

if n in classA:  
    ss += (iteration * 16)

if n in classB:
    if n == 2:
        ss += 7
    else:
        ss += (iteration * 16)

print(ss)
