tc = int(input())

def totalDamage(s):
    charge = 1
    dmg = 0
    for letter in s:
        if letter == 'C':
            charge *= 2
        if letter == 'S':
            dmg += charge
    return dmg

def swapped(p):
    p = p[::-1]
    p = p.replace('SC','CS',1)
    return p[::-1]

def minSwaps(d,p):
    swaps = 0
    if(p.count('S') > d):
        return "IMPOSSIBLE"
    else:
        while(totalDamage(p) > d):
            swaps += 1
            p = swapped(p)
    return swaps

for i in range(tc):
    d, p = [x for x in input().split(' ')]
    d = int(d)
    ans = minSwaps(d,p)
    print("Case #"+str(i+1)+": ",ans)
