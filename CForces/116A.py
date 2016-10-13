tc = input()
capacity = 0
tram = []
for testcase in range(0,int(tc)):
    mov = list((input().split(' ')))
    capacity -= int(mov[0])
    capacity += int(mov[1])
    tram.append(capacity)

print(sorted(tram)[-1])
