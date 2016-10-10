problems = int(input())
c = 0
for i in range(0,problems):
    solutions = list(input().split(' '))
    solutions = [int(elem) for elem in solutions]
    if sum(solutions) >= 2:
        c = c + 1
print(c)

    

