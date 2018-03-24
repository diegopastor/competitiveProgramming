h,u,d,f = [float(x) for x in input().split(' ')]
while(h):
    days = 0
    while(True):
        days += 1
        climbed += u
        if(climbed > h):
            print("success on day "+str(days))
            break;
        u = u*((100.0 - f) / 100.0)
        climbed -= d
        if(climbed <= 0):
            print("failure on day "+str(days))
            break;
    h,u,d,f = [float(x) for x in input().split(' ')]
