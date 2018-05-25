n = int(input())
room = []
c = 0

for i in range(n):
    room.append(input())

s = set(room)
ans =max(room.count(e) for e in s)

print(ans)
