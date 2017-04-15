n, m = [int(x) for x in input().split(' ')]
tasks = [int(x) for x in input().split(' ')]

pos = 1
time = 0

for task in tasks:
    if pos < (task):
        time += task - pos
    elif pos > (task):
        time += (n - pos) + task 

    pos = task

print(time)
