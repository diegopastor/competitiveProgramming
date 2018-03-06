a,b = [int(x) for x in input().split(' ')]

while(a and b):
    if a >= (2*b):
        a = (a - 2*b)
    else:
        if b >= (2*a):
            b = (b - 2*a)
    if(a < (2*b) and b < (2*a)):
        break
    
print(a,b)
