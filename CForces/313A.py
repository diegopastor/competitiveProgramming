m = input()
if int(m) >= 0:
    print(m)
else:
    a = int(m[:len(m)-1])
    b = int(m[:len(m)-2]+m[-1])
    print(max(a,b))
    
