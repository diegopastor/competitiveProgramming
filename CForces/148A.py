#4 days without code and I yield this monster, constancy is king
k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
multiplesOfKToD = [x for x in range(1,d+1) if x % k == 0]
multiplesOfLToD = [x for x in range(1,d+1) if x % l == 0]
multiplesOfMToD = [x for x in range(1,d+1) if x % m == 0]
multiplesOfNToD = [x for x in range(1,d+1) if x % n == 0]

dragons = {key : False for key in range(1,d+1)}

def damageDragons(ls):
    for num in ls:
        if num in dragons:
            dragons[num] = True

damageDragons(multiplesOfKToD)
damageDragons(multiplesOfLToD)
damageDragons(multiplesOfMToD)
damageDragons(multiplesOfNToD)

num_true = sum(dragons.values())
print(num_true)

