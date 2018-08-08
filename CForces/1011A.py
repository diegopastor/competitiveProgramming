n,k = map(int,input().split(' '))
letters = sorted(input())
answer = []

def wOf(answer):
    w = 0
    for letter in answer:
        w += ord(letter) -96
    return w

def iwOf(letter):
    return ord(letter) -96

def difference(a,b):
    return (ord(a)-96) - (ord(b)-96)

i = 1
answer.append(letters[0])
lastLetter = letters[0]

while len(answer) < k:
    if i > len(letters)-1:
        break
    if difference(letters[i],lastLetter) > 1:
        answer.append(letters[i])
        lastLetter = letters[i]
    i += 1

if len(answer) == k:
    print(wOf(answer))
else:
    print(-1)
