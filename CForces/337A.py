n,m = [int(x) for x in input().split(' ')]
puzzles = [int(x) for x in input().split(' ')]
puzzles.sort()

minDif = 9999999999
if m-n == 0:
    minDif = abs(max(puzzles)-min(puzzles))
else:
    for i in range(0,m-n+1):
        minDif = min(minDif,abs(max(puzzles[i:n+i])-min(puzzles[i:n+i])))

print(minDif)
