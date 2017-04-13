n = int(input())
soldiers = [int(x) for x in input().split(' ')]

first = soldiers.index(max(soldiers)) 
soldiers = soldiers[::-1]
lastT = soldiers.index(min(soldiers)) 
soldiers = soldiers[::-1]

for i in range(len(soldiers)-1,-1,-1):
    if soldiers[i] == min(soldiers):
        last = i
        break

if first > last:
    print(first+lastT-1)
else:
    print(first+lastT)
