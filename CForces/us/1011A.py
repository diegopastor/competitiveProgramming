n,k = map(int,input().split(' '))
letters = sorted(input())
weight = 0

def weightOf(letter):
    return ord(letter) - 96

lastLetter = '9'

for i in range(0,k):
    print(letters[i])
    if((ord(letters[i]) - ord(lastLetter)) > 1):
        lastLetter = letters[i]
        weight += weightOf(lastLetter)
    else:
        continue

print(weight)
