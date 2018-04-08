tc = int(input())

def correct(l):
    sl = sorted(l)
    if sl == l:
        return "OK"
    else:
        for i in range(len(l)):
            if l[i] != sl[i]:
                return i

def troublesort(l):
    done = False
    while not done:
        done = True
        for i in range(len(l)-2):
            if l[i] > l[i+2]:
                done = False
                temp = l[i]
                l[i] = l[i+2]
                l[i+2] = temp
    

for i in range(tc):
    n = int(input())
    l = [int(x) for x in input().split(' ')]
    troublesort(l)
    print("Case #"+str(i+1)+": ",correct(l))
