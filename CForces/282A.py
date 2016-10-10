operations = int(input())
x = 0

for i in range(0,operations):
    operation = input()
    if '-' in operation:
        x = x -1
    else: 
        x = x +1

print(x)
