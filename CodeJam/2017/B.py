def tidy(n):
    n = str(n)
    c = 1
    for i in range(len(n)-1):
        if int(n[i]) <= int(n[i+1]):
            c+=1
    if c == len(n):
        return True
    else:
        return False

def subeybaja(s):
    n = str(s)
    sube = False
    baja = False
    for i in range(len(n)-1):
        if int(n[i]) < int(n[i+1]):
            sube = True
        if int(n[i]) > int(n[i+1]):
            baja = True
    if sube == True and baja == True:
        return True
    else: return False

def td(s):
    s = str(s)
    if subeybaja(s):
        last = int(s[2:])
    else:
        last = int(s[1:])
    last += 1
    s = int(s)
    return s - last
            

def tidiser(n):
    if tidy(n):
        return n
    else:
        return td(n)


t = int(input())
for i in range(t):
    n = int(input())
    print("Case #"+str(i+1)+": "+" "+str(tidiser(n)))
